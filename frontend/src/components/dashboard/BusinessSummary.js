export default function BusinessSummary({ analysisData }) {
  const businessSummary =
    analysisData?.dataset?.business_summary;

  if (!businessSummary) {
    return null;
  }

  return (
    <section className="dashboard-section">
      <div className="section-header">
        <div>
          <h2>AI Business Summary</h2>

          <p>
            Complete AI-generated interpretation of your
            dataset and business analysis.
          </p>
        </div>
      </div>

      <div className="business-summary-card">
        <div className="business-summary-header">
          <div className="business-summary-icon">
            ✦
          </div>

          <div>
            <span className="business-summary-label">
              AI GENERATED ANALYSIS
            </span>

            <h3>Complete Dataset Summary</h3>
          </div>
        </div>

        <div className="business-summary-content">
          <p>{businessSummary}</p>
        </div>

        <div className="business-summary-footer">
          Generated from data quality, exploratory analysis,
          correlations, and dataset patterns.
        </div>
      </div>
    </section>
  );
}