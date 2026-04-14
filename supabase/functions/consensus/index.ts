import { serve } from "https://deno.land/std@0.168.0/http/server.ts"

serve(async (req) => {
  try {
    const { proposals } = await req.json()
    
    // Consensus Engine Logic
    // score = confidence^0.4 + expected_return^0.3 + latency_score^0.2 + historical_accuracy^0.1
    
    let bestProposal = null;
    let maxScore = -1;

    for (const p of proposals) {
      const score = Math.pow(p.confidence, 0.4) + 
                    Math.pow(p.expected_return, 0.3) + 
                    Math.pow(p.latency_score, 0.2) + 
                    Math.pow(p.historical_accuracy || 0.5, 0.1);
      
      if (score > maxScore) {
        maxScore = score;
        bestProposal = p;
      }
    }

    if (maxScore < 0.75) {
      return new Response(JSON.stringify({ action: "HOLD", reason: "Score too low" }), {
        headers: { "Content-Type": "application/json" },
      })
    }

    return new Response(JSON.stringify({ ...bestProposal, final_score: maxScore }), {
      headers: { "Content-Type": "application/json" },
    })
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), { status: 400 })
  }
})
