import { useState } from "react";

export default function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function audit() {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/audit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.detail);
      } else {
        setResult(data);
      }
    } catch {
      setError("Unable to connect to backend.");
    }

    setLoading(false);
  }

  const cards = result
    ? [
        ["HTTP Status", result.status],
        ["Response Time", `${result.response_time_ms} ms`],
        ["Page Title", result.title || "N/A"],
        ["Meta Description", result.meta_description || "N/A"],
        ["H1 Count", result.h1_count],
        ["Images Missing Alt", result.missing_alt_images],
        ["Word Count", result.word_count],
      ]
    : [];

  return (
    <div className="min-h-screen bg-slate-100 flex items-center justify-center p-6">
      <div className="w-full max-w-3xl bg-white rounded-2xl shadow-xl p-8">

        <h1 className="text-4xl font-bold text-center">
          🔎 Page Pulse
        </h1>

        <p className="text-center text-gray-500 mt-2">
          Audit any webpage in seconds
        </p>

        <div className="flex gap-3 mt-8">
          <input
            className="flex-1 border rounded-lg p-3"
            placeholder="https://example.com"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />

          <button
            onClick={audit}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 rounded-lg"
          >
            {loading ? "Loading..." : "Audit"}
          </button>
        </div>

        {error && (
          <div className="bg-red-100 text-red-700 mt-6 p-4 rounded-lg">
            {error}
          </div>
        )}

        {result && (
          <div className="grid md:grid-cols-2 gap-4 mt-8">
            {cards.map(([label, value]) => (
              <div
                key={label}
                className="border rounded-xl p-4 bg-slate-50"
              >
                <p className="text-sm text-gray-500">{label}</p>
                <p className="font-semibold mt-1 break-words">{value}</p>
              </div>
            ))}
          </div>
        )}

        <footer className="text-center mt-10 text-gray-500 text-sm">
          Built for Digital Heroes Training Task •{" "}
          <a
            href="https://digitalheroesco.com"
            target="_blank"
            rel="noreferrer"
            className="text-blue-600 underline"
          >
            Digital Heroes
          </a>
        </footer>

      </div>
    </div>
  );
}