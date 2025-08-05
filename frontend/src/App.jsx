import ClerkProviderWithRoutes from "./auth/ClerkProviderWithRoutes.jsx";
import { Routes, Route } from "react-router-dom";
import { Layout } from "./layout/Layout";
import { ChallengeGenerator } from "./challenge/ChallengeGenerator.jsx";
import { HistoryPanel } from "./history/HistoryPanel.jsx";
import { AuthenticationPage } from "./auth/AuthenticationPage.jsx";
import "./App.css";

function App() {
  return (
    <ClerkProviderWithRoutes>
      {/* Your application components go here */}
      <Routes>
        {/* Define your routes here */}
        <Route path="/sign-in/*" element={<AuthenticationPage />} />
        <Route path="/sign-up" element={<AuthenticationPage />} />
        <Route element={<Layout />}>
          <Route path="/" element={<ChallengeGenerator />} />
          <Route path="/history" element={<HistoryPanel />} />
        </Route>
      </Routes>
    </ClerkProviderWithRoutes>
  );
}

export default App;
