export default function AIInsights({ analysisData }) {
  const insights = analysisData?.dataset?.ai_insights;

  if (!insights) {
    return (
      <section className="dashboard-section">
        <div className="section-header">
          <div>
            <h2>AI Insights</h2>
            <p>AI-powered business insights from your dataset.</p>
          </div>
        </div>

        <div className="ai-insights-card">
          <p className="empty-message">
            No AI insights available for this dataset.
          </p>
        </div>
      </section>
    );
  }

  return (
    <section className="dashboard-section">
      <div className="section-header">
        <div>
          <h2>AI Insights</h2>
          <p>
            AI-powered patterns, risks, and business opportunities.
          </p>
        </div>
      </div>

      <div className="ai-insights-grid">
        <div className="ai-insight-card">
          <span className="insight-label">Executive Summary</span>

          <h3>Dataset Overview</h3>

          <p>
            {insights.executive_summary ||
              "No executive summary available."}
          </p>
        </div>

        <div className="ai-insight-card">
          <span className="insight-label">Key Findings</span>

          <h3>Important Patterns</h3>

          <div className="insight-list">
            {insights.key_findings?.length > 0 ? (
              insights.key_findings.map((finding, index) => (
                <p key={index}>• {finding}</p>
              ))
            ) : (
              <p>No key findings available.</p>
            )}
          </div>
        </div>

        <div className="ai-insight-card">
          <span className="insight-label risk-label">
            Business Risks
          </span>

          <h3>Potential Risks</h3>

          <div className="insight-list">
            {insights.business_risks?.length > 0 ? (
              insights.business_risks.map((risk, index) => (
                <p key={index}>• {risk}</p>
              ))
            ) : (
              <p>No business risks detected.</p>
            )}
          </div>
        </div>

        <div className="ai-insight-card">
          <span className="insight-label opportunity-label">
            Opportunities
          </span>

          <h3>Growth Opportunities</h3>

          <div className="insight-list">
            {insights.opportunities?.length > 0 ? (
              insights.opportunities.map((opportunity, index) => (
                <p key={index}>• {opportunity}</p>
              ))
            ) : (
              <p>No opportunities available.</p>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}