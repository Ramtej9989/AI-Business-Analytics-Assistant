"use client";

import { useState } from "react";

import api from "@/services/api";

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
      const response = await api.post("/ask/", {
        question: question.trim(),
      });

      const data = response.data;

      setAnswer(data.ai_answer);
      setQuery(data.pandas_query);
      setResult(data.result);
    } catch (requestError) {
      console.error(
        "Ask Your Data error:",
        requestError
      );

      const errorMessage =
        requestError.response?.data?.detail ||
        requestError.message ||
        "Failed to answer question.";

      setError(errorMessage);
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
            disabled={loading}
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
            disabled={loading}
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
            disabled={loading}
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
            disabled={loading}
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
                <summary>
                  View calculation result
                </summary>

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