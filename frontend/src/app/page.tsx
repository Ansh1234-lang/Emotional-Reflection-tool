"use client";
import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); // prevent page reload
    setLoading(true);
    setResponse("");
    

    const formData = new FormData();
    formData.append("text", text);

    try {
      const res = await fetch("http://127.0.0.1:8000/reflect", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResponse(data.emotion);
    } catch (error) {
      setResponse("Failed to fetch response from backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6 bg-black-50">
      <h1 className="text-2xl font-bold mb-4">Emotion Reflection Tool</h1>

      <form onSubmit={handleSubmit} className="w-full max-w-md space-y-4">
        <textarea
          name="text"
          placeholder="How are you feeling today?"
          className="w-full p-3 border border-gray-300 rounded"
          value={text}
          onChange={(e) => setText(e.target.value)}
          required
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          {loading ? "Reflecting..." : "Reflect Emotion"}
        </button>
      </form>

      {response && (
        <div className="mt-6 text-lg font-semibold text-gray-800">
          Result: {response}
        </div>
      )}
    </main>
  );
  
}
