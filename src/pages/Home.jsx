import { useState } from "react";

import Loader from "../components/Loader";
import MessageForm from "../components/MessageForm";
import ResultCard from "../components/ResultCard";
import { createMessage, fetchPrediction } from "../services/api";

function Home() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (content) => {
    setLoading(true);
    setError("");
    setPrediction(null);

    try {
      const message = await createMessage({ content, source: "whatsapp" });
      const result = await fetchPrediction(message.id);
      setPrediction(result);
    } catch (apiError) {
      const message =
        apiError?.response?.status === 401
          ? "Unauthorized request. Add a valid JWT token in localStorage as 'token' or update backend auth settings."
          : apiError?.response?.data?.detail || "Could not analyze the message right now. Please try again.";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section>
      <div className="mb-6">
        <h2 className="text-3xl font-bold text-slate-900">AI Fraud Detection System</h2>
        <p className="mt-2 text-sm text-slate-600">
          Submit suspicious text and get a fraud risk result with confidence and explanation.
        </p>
      </div>

      <MessageForm onSubmit={handleSubmit} disabled={loading} />

      {loading && <div className="mt-4"><Loader /></div>}

      {error && (
        <div className="mt-4 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          {error}
        </div>
      )}

      {prediction && <ResultCard prediction={prediction} />}
    </section>
  );
}

export default Home;
