import { useState } from "react";

function MessageForm({ onSubmit, disabled }) {
  const [content, setContent] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!content.trim()) return;
    onSubmit(content.trim());
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <label htmlFor="message" className="block text-sm font-medium text-slate-700">
        Enter SMS, WhatsApp text, job offer, or any suspicious message
      </label>
      <textarea
        id="message"
        className="min-h-36 w-full rounded-md border border-slate-300 px-3 py-2 text-sm outline-none ring-indigo-200 placeholder:text-slate-400 focus:ring"
        placeholder="Example: Earn money daily! No skills needed. Registration fee required."
        value={content}
        onChange={(event) => setContent(event.target.value)}
        disabled={disabled}
      />
      <button
        type="submit"
        disabled={disabled || !content.trim()}
        className="inline-flex items-center rounded-md bg-indigo-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-indigo-700 disabled:cursor-not-allowed disabled:bg-indigo-300"
      >
        {disabled ? "Analyzing..." : "Check Fraud Risk"}
      </button>
    </form>
  );
}

export default MessageForm;
