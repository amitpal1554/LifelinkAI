import React from "react";
import { Link } from "react-router-dom";

function Approach() {
  return (
    <section id="approach" className="ll-approach">
      <div className="ll-approach-panel">
        <div className="ll-approach-copy">
          <p className="ll-tag ll-tag-plain">Our approach</p>
          <h2 className="ll-display">
            Human-centred AI that supports — never replaces — clinical judgement
          </h2>
          <p>
            Every prediction is designed as a decision aid: transparent inputs,
            clear outputs, and workflows that keep clinicians in control.
          </p>
        </div>
        <Link to="/predictors" className="ll-btn-primary ll-approach-cta">
          Explore predictors
        </Link>
      </div>
    </section>
  );
}

export default Approach;
