function Navbar() {
  return (
    <header className="border-b border-slate-200 bg-white">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
        <h1 className="text-lg font-bold text-slate-900">AI Fraud Detection System</h1>
        <span className="rounded-full bg-indigo-50 px-3 py-1 text-sm font-medium text-indigo-700">FastAPI Connected</span>
      </div>
    </header>
  );
}

export default Navbar;
