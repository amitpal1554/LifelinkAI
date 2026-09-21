import React from "react";
import Hero from "../components/Hero";
import Capabilities from "../components/Capabilities";
import Approach from "../components/Approach";
import SiteFooter from "../components/SiteFooter";

function HomePage() {
  return (
    <div className="ll-home">
      <Hero />
      <Capabilities />
      <Approach />
      <SiteFooter />
    </div>
  );
}

export default HomePage;
