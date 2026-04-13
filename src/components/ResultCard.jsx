const colorMap = {
  safe: {
    accent: "text-emerald-700",
    bg: "bg-emerald-50",
    ring: "ring-emerald-200",
    label: "Safe",
  },
  scam: {
    accent: "text-red-700",
    bg: "bg-red-50",
    ring: "ring-red-200",
    label: "Scam",
  },
  suspicious: {
    accent: "text-amber-700",
    bg: "bg-amber-50",
    ring: "ring-amber-200",
    label: "Suspicious",
  },
};

function resolveStatus(result, confidence) {
  if (result === "safe" && confidence < 0.65) return "suspicious";
  if (result === "scam") return "scam";
  return "safe";
}

function ResultCard({ prediction }) {
  const status = resolveStatus(prediction.result, prediction.confidence);
  const colors = colorMap[status];

  return (
    <section className={`mt-6 rounded-xl p-6 ring-1 ${colors.bg} ${colors.ring}`}>
      <h2 className={`text-xl font-semibold ${colors.accent}`}>Result: {colors.label}</h2>
      <dl className="mt-4 grid gap-3 text-sm sm:grid-cols-2">
        <div>
          <dt className="font-medium text-slate-600">Confidence</dt>
          <dd className="text-slate-900">{Math.round(prediction.confidence * 100)}%</dd>
        </div>
        <div>
          <dt className="font-medium text-slate-600">Category</dt>
          <dd className="text-slate-900 capitalize">{prediction.category.replaceAll("_", " ")}</dd>
        </div>
      </dl>
      <div className="mt-4 rounded-md bg-white/70 p-4">
        <p className="text-sm font-medium text-slate-700">Explanation</p>
        <p className="mt-1 text-sm text-slate-800">{prediction.explanation}</p>
      </div>
    </section>
  );
}

export default ResultCard;
