import React from "react";
import { Link } from "react-router-dom";
import heartImg from "../assets/heart.png";
import diabetesImg from "../assets/diabetes.png";
import lungImg from "../assets/lung.png";

const features = [
  {
    id: "prediction",
    image: heartImg,
    label: "Prediction",
    title: "Multi-disease AI models",
    text: "Heart, diabetes, breast and lung predictors designed to surface risk signals early and clearly.",
    to: "/predictors",
  },
  {
    id: "monitoring",
    image: diabetesImg,
    label: "Monitoring",
    title: "Health signals in context",
    text: "Turn clinical inputs into readable insights that support faster, more confident decisions.",
    to: "/predictors",
  },
  {
    id: "diagnostics",
    image: lungImg,
    label: "Diagnostics",
    title: "Rapid diagnostic suite",
    text: "From form-based screening to image analysis — one flow for multi-disease assessment.",
    to: "/predictors",
  },
];

function Capabilities() {
  return (
    <section id="capabilities" className="ll-capabilities">
      <div className="ll-section-inner">
        <div className="ll-section-intro">
          <p className="ll-tag ll-tag-plain">Capabilities</p>
          <h2 className="ll-display ll-section-title">
            Connected intelligence for care teams
          </h2>
          <p className="ll-section-desc">
            LifelinkAI brings prediction, monitoring and diagnostics together so
            clinicians can act with clarity — not noise.
          </p>
        </div>

        <div className="ll-feature-grid">
          {features.map((feature) => (
            <Link
              key={feature.id}
              to={feature.to}
              className="ll-feature-card"
            >
              <div className="ll-feature-media image-wash">
                <img src={feature.image} alt="" loading="lazy" />
              </div>
              <div className="ll-feature-body">
                <p className="ll-tag ll-tag-plain">{feature.label}</p>
                <h3>{feature.title}</h3>
                <p>{feature.text}</p>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Capabilities;
