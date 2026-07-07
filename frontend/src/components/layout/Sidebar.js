"use client";

import { useEffect, useState } from "react";

const navigationItems = [
  {
    label: "Dashboard",
    sectionId: "dashboard",
  },
  {
    label: "Data Quality",
    sectionId: "data-quality",
  },
  {
    label: "AI Insights",
    sectionId: "ai-insights",
  },
  {
    label: "Charts",
    sectionId: "charts",
  },
  {
    label: "Ask Your Data",
    sectionId: "ask-your-data",
  },
];

export default function Sidebar() {
  const [activeSection, setActiveSection] =
    useState("dashboard");

  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY + 180;

      let currentSection = "dashboard";

      navigationItems.forEach((item) => {
        const section = document.getElementById(
          item.sectionId
        );

        if (
          section &&
          section.offsetTop <= scrollPosition
        ) {
          currentSection = item.sectionId;
        }
      });

      const isAtBottom =
        window.innerHeight + window.scrollY >=
        document.documentElement.scrollHeight - 10;

      if (isAtBottom) {
        currentSection = "ask-your-data";
      }

      setActiveSection(currentSection);
    };

    window.addEventListener("scroll", handleScroll);

    handleScroll();

    return () => {
      window.removeEventListener(
        "scroll",
        handleScroll
      );
    };
  }, []);

  useEffect(() => {
    if (isMenuOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }

    return () => {
      document.body.style.overflow = "";
    };
  }, [isMenuOpen]);

  const scrollToSection = (sectionId) => {
    const section = document.getElementById(sectionId);

    if (section) {
      setActiveSection(sectionId);
      setIsMenuOpen(false);

      section.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  };

  return (
    <>
      <header className="mobile-header">
        <div className="mobile-brand">
          <h2>AI Analytics</h2>
          <p>Business Assistant</p>
        </div>

        <button
          type="button"
          className="mobile-menu-button"
          onClick={() => setIsMenuOpen(true)}
          aria-label="Open navigation menu"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </header>

      {isMenuOpen && (
        <div
          className="sidebar-overlay"
          onClick={() => setIsMenuOpen(false)}
        />
      )}

      <aside
        className={
          isMenuOpen
            ? "sidebar sidebar-open"
            : "sidebar"
        }
      >
        <div className="sidebar-top">
          <div className="sidebar-brand">
            <h2>AI Analytics</h2>
            <p>Business Assistant</p>
          </div>

          <button
            type="button"
            className="sidebar-close-button"
            onClick={() => setIsMenuOpen(false)}
            aria-label="Close navigation menu"
          >
            ×
          </button>
        </div>

        <nav className="sidebar-nav">
          {navigationItems.map((item) => (
            <p
              key={item.sectionId}
              className={
                activeSection === item.sectionId
                  ? "active"
                  : ""
              }
              onClick={() =>
                scrollToSection(item.sectionId)
              }
            >
              {item.label}
            </p>
          ))}
        </nav>
      </aside>
    </>
  );
}