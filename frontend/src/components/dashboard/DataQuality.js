export default function DataQuality({ analysisData }) {
  const dataset = analysisData.dataset;
  const dataQuality = dataset.data_quality;
  const recommendations = dataset.cleaning_recommendations;

  return (
    <section className="dashboard-section">
      <div className="section-header">
        <div>
          <h2>Data Quality</h2>
          <p>
            Dataset health, missing values, and cleaning recommendations.
          </p>
        </div>

        <div className="quality-score">
          <span>Quality Score</span>
          <strong>{dataQuality.quality_score}%</strong>
        </div>
      </div>

      <div className="quality-grid">
        <div className="quality-card">
          <p>Total Missing Values</p>
          <h3>{dataQuality.total_missing_values.toLocaleString()}</h3>
          <span>{dataQuality.missing_percentage}% of dataset</span>
        </div>

        <div className="quality-card">
          <p>Duplicate Rows</p>
          <h3>{dataQuality.duplicate_rows.toLocaleString()}</h3>
          <span>Duplicate records detected</span>
        </div>

        <div className="quality-card">
          <p>Duplicate Columns</p>
          <h3>{dataQuality.duplicate_columns.length}</h3>
          <span>Duplicate columns detected</span>
        </div>

        <div className="quality-card">
          <p>Constant Columns</p>
          <h3>{dataQuality.constant_columns.length}</h3>
          <span>Columns with one unique value</span>
        </div>
      </div>

      <div className="recommendations-card">
        <h3>Cleaning Recommendations</h3>

        {recommendations.length === 0 ? (
          <p className="empty-message">
            No cleaning recommendations found.
          </p>
        ) : (
          <div className="recommendations-list">
            {recommendations.map((recommendation, index) => (
              <div
                className="recommendation-item"
                key={`${recommendation.column}-${index}`}
              >
                <div>
                  <strong>{recommendation.column}</strong>

                  <p>{recommendation.recommendation}</p>
                </div>

                <span>
                  {recommendation.missing_percentage}% missing
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}