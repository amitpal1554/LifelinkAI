import React from "react";
import { Link } from "react-router-dom";
import { FiActivity, FiArrowRight, FiShield } from "react-icons/fi";
import heroCareImage from "../assets/hero-doctor-patient.jpg";

function Hero() {
  return (
    <section id="home" className="ll-hero">
      <div className="ll-hero-grid" aria-hidden="true" />
      <div className="ll-orb ll-orb-right" aria-hidden="true" />
      <div className="ll-orb ll-orb-left" aria-hidden="true" />

      <div className="ll-hero-inner">
        <div className="ll-hero-copy">
          <p className="ll-tag">Intelligent health signals</p>
          <h1 className="ll-display">
            Clarity for every
            <br />
            moment of care.
          </h1>
          <p className="ll-hero-desc">
            LifelinkAI helps clinical teams turn continuous health data into
            timely, human-centred decisions.
          </p>
          <div className="ll-hero-actions">
            <Link to="/predictors" className="ll-btn-primary">
              <span>Diagnose Now</span>
              <FiArrowRight size={17} />
            </Link>
          </div>
          <div className="ll-hero-note">
            <span className="ll-note-icon">
              <FiShield size={18} />
            </span>
            <p>
              Built to support care teams — never replace clinical judgement.
            </p>
          </div>
        </div>

        <div className="ll-hero-art">
          <div className="ll-art-back" aria-hidden="true" />
          <div className="ll-art-dashed" aria-hidden="true" />
          <div className="ll-image-wash">
            <img
              src={heroCareImage}
              alt="Doctor consulting with a patient"
              loading="lazy"
            />
            <div className="ll-signal-card">
              <div>
                <p className="ll-signal-label">Care signal</p>
                <p className="ll-signal-value">Meaningful insight, in context</p>
              </div>
              <span className="ll-signal-icon">
                <FiActivity size={20} />
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
