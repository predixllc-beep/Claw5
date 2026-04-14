'use client';

import { useState, useEffect } from 'react';
import { motion } from 'motion/react';

export default function Home() {
  const [logs, setLogs] = useState<string[]>([]);

  useEffect(() => {
    const interval = setInterval(() => {
      setLogs(prev => [...prev, `[${new Date().toISOString()}] Agent sync complete. Latency: ${Math.random() * 10}ms`].slice(-10));
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-black text-green-500 font-mono">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm"
      >
        <h1 className="text-4xl font-bold mb-8 text-center text-green-400 drop-shadow-[0_0_10px_rgba(0,255,0,0.8)]">
          NEXUS CLAW V3
        </h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
          <div className="border border-green-500/30 p-6 rounded-lg bg-black/50 backdrop-blur-sm">
            <h2 className="text-xl font-semibold mb-4 text-green-300">Swarm Status</h2>
            <div className="space-y-2">
              <div className="flex justify-between"><span>Data Agents:</span> <span className="text-green-400">ONLINE</span></div>
              <div className="flex justify-between"><span>Strategy Swarm:</span> <span className="text-green-400">ACTIVE</span></div>
              <div className="flex justify-between"><span>Consensus Engine:</span> <span className="text-green-400">SYNCED</span></div>
              <div className="flex justify-between"><span>Risk Engine:</span> <span className="text-green-400">ARMED</span></div>
            </div>
          </div>

          <div className="border border-green-500/30 p-6 rounded-lg bg-black/50 backdrop-blur-sm overflow-hidden flex flex-col">
            <h2 className="text-xl font-semibold mb-4 text-green-300">Live Telemetry</h2>
            <div className="flex-1 overflow-y-auto space-y-1 text-xs text-green-500/80">
              {logs.map((log, i) => (
                <div key={i}>{log}</div>
              ))}
            </div>
          </div>
        </div>
      </motion.div>
    </main>
  );
}
