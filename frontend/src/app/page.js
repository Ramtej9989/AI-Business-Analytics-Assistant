"use client";

import { useState } from "react";

import DatasetUpload from "@/components/upload/DatasetUpload";
import Sidebar from "@/components/layout/Sidebar";
import DashboardHeader from "@/components/dashboard/DashboardHeader";
import OverviewCards from "@/components/dashboard/OverviewCards";
import DataQuality from "@/components/dashboard/DataQuality";
import AIInsights from "@/components/dashboard/AIInsights";
import BusinessSummary from "@/components/dashboard/BusinessSummary";
import Charts from "@/components/dashboard/Charts";
import AskYourData from "@/components/dashboard/AskYourData";

export default function Home() {
  const [analysisData, setAnalysisData] = useState(null);

  if (!analysisData) {
    return (
      <main className="upload-page">
        <div className="upload-container">
          <div className="upload-page-badge">
            AI-POWERED ANALYTICS
          </div>

          <h1>
            Turn your data into
            <span> business insights.</span>
          </h1>

          <p className="upload-page-description">
            Upload your business dataset and let AI analyze
            data quality, patterns, correlations, risks, and
            growth opportunities.
          </p>

          <DatasetUpload
            onUploadSuccess={setAnalysisData}
          />

          <div className="upload-features">
            <span>Data Quality</span>
            <span>AI Insights</span>
            <span>Smart Charts</span>
            <span>Ask Your Data</span>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="dashboard-layout">
      <Sidebar />

      <section className="dashboard-content">
        <div
          id="dashboard"
          className="scroll-section"
        >
          <DashboardHeader
            analysisData={analysisData}
          />

          <OverviewCards
            analysisData={analysisData}
          />
        </div>

        <div
          id="data-quality"
          className="scroll-section"
        >
          <DataQuality
            analysisData={analysisData}
          />
        </div>

        <div
          id="ai-insights"
          className="scroll-section"
        >
          <AIInsights
            analysisData={analysisData}
          />
        </div>

        <div
          id="business-summary"
          className="scroll-section"
        >
          <BusinessSummary
            analysisData={analysisData}
          />
        </div>

        <div
          id="charts"
          className="scroll-section"
        >
          <Charts
            analysisData={analysisData}
          />
        </div>

        <div
          id="ask-your-data"
          className="scroll-section"
        >
          <AskYourData />
        </div>
      </section>
    </main>
  );
}