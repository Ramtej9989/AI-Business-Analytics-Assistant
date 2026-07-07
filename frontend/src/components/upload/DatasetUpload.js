"use client";

import { useRef, useState } from "react";

import api from "@/services/api";

const allowedExtensions = ["csv", "xlsx", "xls"];

export default function DatasetUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState("");

  const fileInputRef = useRef(null);

  const validateAndSetFile = (selectedFile) => {
    if (!selectedFile) {
      return;
    }

    const extension = selectedFile.name
      .split(".")
      .pop()
      ?.toLowerCase();

    if (!allowedExtensions.includes(extension)) {
      setFile(null);
      setError(
        "Unsupported file format. Please upload CSV, XLSX, or XLS."
      );
      return;
    }

    setFile(selectedFile);
    setError("");
  };

  const handleFileChange = (event) => {
    validateAndSetFile(event.target.files[0]);
  };

  const handleDragEnter = (event) => {
    event.preventDefault();
    event.stopPropagation();

    setIsDragging(true);
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    event.stopPropagation();

    setIsDragging(true);
  };

  const handleDragLeave = (event) => {
    event.preventDefault();
    event.stopPropagation();

    setIsDragging(false);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    event.stopPropagation();

    setIsDragging(false);

    validateAndSetFile(event.dataTransfer.files[0]);
  };

  const handleBrowseClick = () => {
    fileInputRef.current?.click();
  };

  const handleRemoveFile = (event) => {
    event.stopPropagation();

    setFile(null);
    setError("");

    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a dataset first.");
      return;
    }

    setIsUploading(true);
    setError("");

    const formData = new FormData();

    formData.append("file", file);

    try {
      const response = await api.post(
        "/upload/",
        formData
      );

      onUploadSuccess(response.data);
    } catch (uploadError) {
      console.error("Upload error:", uploadError);

      const errorMessage =
        uploadError.response?.data?.detail ||
        uploadError.message ||
        "Failed to upload dataset.";

      setError(errorMessage);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <section className="dataset-upload">
      <div
        className={
          isDragging
            ? "upload-dropzone upload-dropzone-active"
            : "upload-dropzone"
        }
        onClick={handleBrowseClick}
        onDragEnter={handleDragEnter}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        role="button"
        tabIndex={0}
        onKeyDown={(event) => {
          if (
            event.key === "Enter" ||
            event.key === " "
          ) {
            handleBrowseClick();
          }
        }}
      >
        <input
          ref={fileInputRef}
          className="upload-file-input"
          type="file"
          accept=".csv,.xlsx,.xls"
          onChange={handleFileChange}
        />

        <div className="upload-icon">
          <svg
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <path
              d="M12 16V4M12 4L7.5 8.5M12 4l4.5 4.5M5 14v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-4"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.8"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </div>

        {!file ? (
          <>
            <h3>Drag & drop your dataset</h3>

            <p>
              Drop your file here or{" "}
              <span>browse from your device</span>
            </p>

            <small>
              Supports CSV, XLSX and XLS files
            </small>
          </>
        ) : (
          <div className="selected-file">
            <div className="selected-file-info">
              <strong>{file.name}</strong>

              <span>
                {(file.size / 1024 / 1024).toFixed(2)} MB
              </span>
            </div>

            <button
              type="button"
              className="remove-file-button"
              onClick={handleRemoveFile}
              aria-label="Remove selected file"
            >
              ×
            </button>
          </div>
        )}
      </div>

      {error && (
        <div className="upload-error-message">
          {error}
        </div>
      )}

      <button
        type="button"
        className="analyze-dataset-button"
        onClick={handleUpload}
        disabled={isUploading || !file}
      >
        {isUploading ? (
          <>
            <span className="upload-spinner" />
            Analyzing Dataset...
          </>
        ) : (
          "Analyze Dataset"
        )}
      </button>
    </section>
  );
}