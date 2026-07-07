export default function DashboardHeader({ analysisData }) {
  return (
    <header className="dashboard-header">
      <div>
        <h1>Analytics Dashboard</h1>

        <p>
          AI-powered insights for your business dataset.
        </p>
      </div>

      <div className="active-dataset">
        <p>Active Dataset</p>

        <strong>
          {analysisData.dataset.filename}
        </strong>
      </div>
    </header>
  );
}