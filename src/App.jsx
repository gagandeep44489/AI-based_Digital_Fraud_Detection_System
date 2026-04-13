import Navbar from "./components/Navbar";
import Home from "./pages/Home";

function App() {
  return (
    <div className="min-h-screen bg-slate-100 text-slate-900">
      <Navbar />
      <main className="mx-auto max-w-4xl px-4 py-8">
        <Home />
      </main>
    </div>
  );
}

export default App;
