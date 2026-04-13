function Loader() {
  return (
    <div className="flex items-center gap-3 rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <div className="h-5 w-5 animate-spin rounded-full border-2 border-indigo-200 border-t-indigo-600" />
      <p className="text-sm text-slate-600">Analyzing message for fraud signals...</p>
    </div>
  );
}

export default Loader;
