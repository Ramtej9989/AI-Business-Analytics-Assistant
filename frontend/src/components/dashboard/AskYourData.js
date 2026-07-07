"use client";

import { useState } from "react";

export default function AskYourData() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState(null);
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAskQuestion = async (event) => {
    event.preventDefault();

    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setError("");
    setAnswer(null);
    setQuery("");
    setResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/ask/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: question.trim(),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Failed to answer question."
        );
      }

      setAnswer(data.ai_answer);
      setQuery(data.pandas_query);
      setResult(data.result);
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="dashboard-section">
      <div className="section-header">
        <div>
          <h2>Ask Your Data</h2>

          <p>
            Ask business questions and get AI-powered answers
            from your dataset.
          </p>
        </div>
      </div>

      <div className="ask-data-card">
        <form
          className="ask-data-form"
          onSubmit={handleAskQuestion}
        >
          <input
            type="text"
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            placeholder="Example: What is the churn rate?"
            disabled={loading}
          />

          <button
            type="submit"
            disabled={loading || !question.trim()}
          >
            {loading ? "Analyzing..." : "Ask AI"}
          </button>
        </form>

        <div className="question-suggestions">
          <button
            type="button"
            onClick={() =>
              setQuestion("What is the churn rate?")
            }
          >
            What is the churn rate?
          </button>

          <button
            type="button"
            onClick={() =>
              setQuestion(
                "What is the average monthly charge?"
              )
            }
          >
            Average monthly charge
          </button>

          <button
            type="button"
            onClick={() =>
              setQuestion(
                "Which contract type has the most customers?"
              )
            }
          >
            Top contract type
          </button>

          <button
            type="button"
            onClick={() =>
              setQuestion(
                "Which internet service is most popular?"
              )
            }
          >
            Popular internet service
          </button>
        </div>

        {error && (
          <div className="ask-error">
            <p>{error}</p>
          </div>
        )}

        {answer && (
          <div className="ask-answer">
            <span className="answer-label">
              AI Answer
            </span>

            <h3>Analysis Result</h3>

            <p>{answer}</p>

            {query && (
              <div className="generated-query">
                <span>Generated Pandas Query</span>

                <code>{query}</code>
              </div>
            )}

            {result !== null && (
              <details className="raw-result">
                <summary>View calculation result</summary>

                <pre>
                  {JSON.stringify(result, null, 2)}
                </pre>
              </details>
            )}
          </div>
        )}
      </div>
    </section>
  );
}