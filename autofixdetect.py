#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           AUTOFIXDETECT AI v10.0 - ULTIMATE FINAL EDITION                  ║
║                                                                            ║
║   ⚡ AI-Powered System Diagnostic & Auto-Fix Tool                          ║
║   🧠 Self-Learning with Internet Search & Improvisation                   ║
║   🌐 Full Web Interface with Real-Time Progress                           ║
║   📚 No External Dependencies - Fully Self-Contained                      ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import platform
import subprocess
import json
import time
import shutil
import socket
import re
import threading
import uuid
import urllib.request
import urllib.parse
import ssl
import hashlib
import signal
import tempfile
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Optional, Any, Set, Tuple
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

#===============================================================================
# VERSION INFORMATION
#===============================================================================
VERSION = "10.0"
VERSION_NAME = "Ultimate Final Edition"
RELEASE_DATE = "2026-09-08"

#===============================================================================
# COLOR SYSTEM
#===============================================================================
class Colors:
    """Advanced color system with fallback for non-terminal environments"""
    def __init__(self):
        self.use_colors = sys.stdout.isatty() and os.environ.get('TERM') != 'dumb'
        if self.use_colors:
            self.RED = '\033[0;31m'
            self.GREEN = '\033[0;32m'
            self.YELLOW = '\033[1;33m'
            self.BLUE = '\033[0;34m'
            self.CYAN = '\033[0;36m'
            self.WHITE = '\033[1;37m'
            self.BOLD = '\033[1m'
            self.DIM = '\033[2m'
            self.NC = '\033[0m'
            self.PURPLE = '\033[0;35m'
            self.ORANGE = '\033[38;5;208m'
            self.PINK = '\033[38;5;205m'
            self.UNDERLINE = '\033[4m'
            self.BLINK = '\033[5m'
            self.REVERSE = '\033[7m'
        else:
            self.RED = self.GREEN = self.YELLOW = self.BLUE = ''
            self.CYAN = self.WHITE = self.BOLD = self.DIM = self.NC = ''
            self.PURPLE = self.ORANGE = self.PINK = self.UNDERLINE = ''
            self.BLINK = self.REVERSE = ''

#===============================================================================
# GLOBAL INSTANCE
#===============================================================================
colors = Colors()

#===============================================================================
# EMBEDDED WEB UI - ULTIMATE VERSION
#===============================================================================
WEB_UI_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AutoFixDetect AI v10.0 - Ultimate</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --bg-primary: #0a0a1a;
            --bg-secondary: #12122a;
            --bg-card: rgba(255,255,255,0.03);
            --border-color: rgba(255,255,255,0.06);
            --text-primary: #ffffff;
            --text-secondary: rgba(255,255,255,0.6);
            --accent-1: #00d2ff;
            --accent-2: #3a7bd5;
            --accent-3: #7c3aed;
            --success: #4ade80;
            --warning: #fbbf24;
            --danger: #f87171;
            --info: #60a5fa;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 20px;
            background-image: 
                radial-gradient(ellipse at 10% 20%, rgba(0,210,255,0.05) 0%, transparent 50%),
                radial-gradient(ellipse at 90% 80%, rgba(124,58,237,0.05) 0%, transparent 50%);
        }
        .container { max-width: 1300px; margin: 0 auto; }
        
        /* Header */
        .header {
            text-align: center;
            padding: 25px 0 30px;
            border-bottom: 1px solid var(--border-color);
            position: relative;
        }
        .header .version-badge {
            display: inline-block;
            padding: 4px 16px;
            border-radius: 20px;
            font-size: 0.7em;
            font-weight: 600;
            background: linear-gradient(45deg, var(--accent-1), var(--accent-3));
            color: #fff;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }
        .header h1 {
            font-size: 2.8em;
            font-weight: 800;
            background: linear-gradient(45deg, var(--accent-1), var(--accent-2), var(--accent-3));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .header .subtitle {
            color: var(--text-secondary);
            margin-top: 8px;
            font-size: 1.1em;
        }
        .header .features {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 15px;
            font-size: 0.85em;
            color: var(--text-secondary);
        }
        .header .features span {
            padding: 4px 12px;
            border-radius: 12px;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
        }
        
        /* Dashboard */
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 15px;
            margin: 25px 0;
        }
        .card {
            background: var(--bg-card);
            backdrop-filter: blur(10px);
            padding: 18px 15px;
            border-radius: 14px;
            border: 1px solid var(--border-color);
            text-align: center;
            transition: all 0.3s ease;
        }
        .card:hover { transform: translateY(-3px); border-color: rgba(255,255,255,0.1); }
        .card .icon { font-size: 1.5em; margin-bottom: 5px; }
        .card h3 { font-size: 0.65em; opacity: 0.5; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
        .card .value { font-size: 2.2em; font-weight: 700; }
        .card .sub { font-size: 0.7em; opacity: 0.5; margin-top: 4px; }
        .card.green .value { color: var(--success); }
        .card.yellow .value { color: var(--warning); }
        .card.red .value { color: var(--danger); }
        .card.blue .value { color: var(--info); }
        .card.purple .value { color: var(--accent-3); }
        .card.cyan .value { color: var(--accent-1); }
        
        /* Progress Bar */
        .progress-section {
            background: var(--bg-card);
            border-radius: 14px;
            padding: 20px;
            margin: 15px 0;
            border: 1px solid var(--border-color);
            display: none;
        }
        .progress-section.active { display: block; }
        .progress-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }
        .progress-title { font-weight: 600; font-size: 0.95em; }
        .progress-title .highlight { color: var(--accent-1); }
        .progress-percent { font-size: 1.4em; font-weight: 700; color: var(--accent-1); }
        .progress-track {
            width: 100%;
            height: 10px;
            background: rgba(255,255,255,0.06);
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        }
        .progress-track .fill {
            height: 100%;
            border-radius: 6px;
            transition: width 0.4s ease;
            width: 0%;
            background: linear-gradient(45deg, var(--accent-1), var(--accent-3));
        }
        .progress-track .fill.complete { background: linear-gradient(45deg, var(--success), #16a34a); }
        .progress-track .fill.error { background: linear-gradient(45deg, var(--danger), #dc2626); }
        .progress-status {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            font-size: 0.85em;
            color: var(--text-secondary);
        }
        .progress-details {
            margin-top: 15px;
            padding: 12px;
            background: rgba(0,0,0,0.3);
            border-radius: 10px;
            max-height: 180px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.8em;
            line-height: 1.6;
        }
        .progress-details::-webkit-scrollbar { width: 4px; }
        .progress-details::-webkit-scrollbar-track { background: rgba(255,255,255,0.03); border-radius: 2px; }
        .progress-details::-webkit-scrollbar-thumb { background: var(--accent-2); border-radius: 2px; }
        .detail-item { padding: 3px 0; border-bottom: 1px solid rgba(255,255,255,0.02); }
        .detail-item.success { color: var(--success); }
        .detail-item.error { color: var(--danger); }
        .detail-item.info { color: var(--info); }
        .detail-item.warn { color: var(--warning); }
        .detail-item.ai { color: var(--accent-3); }
        
        /* Buttons */
        .btn-group {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px 0;
        }
        .btn {
            padding: 10px 28px;
            border: none;
            border-radius: 25px;
            font-size: 0.95em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #fff;
            position: relative;
            overflow: hidden;
        }
        .btn::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255,255,255,0.2);
            transition: all 0.5s ease;
            transform: translate(-50%, -50%);
        }
        .btn:active::after {
            width: 300px;
            height: 300px;
        }
        .btn-primary { background: linear-gradient(45deg, var(--accent-1), var(--accent-2)); }
        .btn-success { background: linear-gradient(45deg, var(--success), #16a34a); }
        .btn-danger { background: linear-gradient(45deg, var(--danger), #dc2626); }
        .btn-warning { background: linear-gradient(45deg, var(--warning), #f59e0b); color: #000; }
        .btn-purple { background: linear-gradient(45deg, var(--accent-3), #6d28d9); }
        .btn:hover { transform: scale(1.04); box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        .btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }
        
        /* Status */
        .status-section {
            background: var(--bg-card);
            border-radius: 14px;
            padding: 18px 20px;
            margin: 15px 0;
            border: 1px solid var(--border-color);
        }
        .status-section h3 {
            font-size: 0.85em;
            opacity: 0.6;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .status-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.03);
        }
        .status-item:last-child { border-bottom: none; }
        .status-badge {
            padding: 3px 14px;
            border-radius: 15px;
            font-size: 0.65em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .status-badge.ok { background: rgba(74,222,128,0.15); color: var(--success); }
        .status-badge.warn { background: rgba(251,191,36,0.15); color: var(--warning); }
        .status-badge.error { background: rgba(248,113,113,0.15); color: var(--danger); }
        .status-badge.running { background: rgba(96,165,250,0.15); color: var(--info); animation: pulse 1.2s infinite; }
        .status-badge.ai { background: rgba(124,58,237,0.15); color: var(--accent-3); }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        /* Error Summary */
        .error-summary {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            padding: 12px 16px;
            background: rgba(0,0,0,0.2);
            border-radius: 10px;
            margin-top: 10px;
        }
        .error-summary .item { font-size: 0.85em; }
        .error-summary .count { font-weight: 700; }
        .error-summary .count.critical { color: var(--danger); }
        .error-summary .count.warning { color: var(--warning); }
        .error-summary .count.info { color: var(--info); }
        
        /* Logs */
        .logs {
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 15px;
            max-height: 180px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.78em;
            line-height: 1.5;
            margin-top: 10px;
        }
        .logs::-webkit-scrollbar { width: 4px; }
        .logs::-webkit-scrollbar-track { background: rgba(255,255,255,0.03); border-radius: 2px; }
        .logs::-webkit-scrollbar-thumb { background: var(--accent-2); border-radius: 2px; }
        .log-entry { padding: 2px 0; border-bottom: 1px solid rgba(255,255,255,0.02); }
        .log-entry .time { color: var(--text-secondary); opacity: 0.5; }
        .log-entry.info { color: var(--success); }
        .log-entry.warn { color: var(--warning); }
        .log-entry.error { color: var(--danger); }
        .log-entry.ai { color: var(--accent-3); }
        .log-entry.progress { color: var(--info); }
        
        /* Responsive */
        @media (max-width: 768px) {
            .header h1 { font-size: 2em; }
            .dashboard { grid-template-columns: repeat(3, 1fr); gap: 10px; }
            .card { padding: 12px 10px; }
            .card .value { font-size: 1.6em; }
            .btn-group { flex-direction: column; }
            .btn { width: 100%; }
            .header .features { font-size: 0.7em; gap: 8px; }
        }
        @media (max-width: 480px) {
            .dashboard { grid-template-columns: repeat(2, 1fr); }
            .header h1 { font-size: 1.5em; }
            body { padding: 10px; }
        }
    </style>
</head>
<body>
<div class="container">
    <!-- Header -->
    <div class="header">
        <div class="version-badge">⚡ v10.0 ULTIMATE</div>
        <h1>🛠 AutoFixDetect AI</h1>
        <div class="subtitle">AI-Powered Self-Learning System Diagnostic & Auto-Fix</div>
        <div class="features">
            <span>🧠 AI Improvisation</span>
            <span>🌐 Internet Search</span>
            <span>📚 Self-Learning</span>
            <span>⚡ Real-Time Progress</span>
        </div>
        <div class="btn-group">
            <button class="btn btn-primary" onclick="runDiagnostic()" id="runBtn">🔍 Scan System</button>
            <button class="btn btn-success" onclick="runFix()" id="fixBtn" disabled>🧠 AI Fix All</button>
            <button class="btn btn-warning" onclick="runFixFast()" id="fastBtn" disabled>⚡ Fast Fix</button>
            <button class="btn btn-danger" onclick="stopFix()" id="stopBtn" disabled>⏹ Stop</button>
            <button class="btn btn-purple" onclick="clearLogs()">🗑 Clear Logs</button>
        </div>
    </div>

    <!-- Dashboard -->
    <div class="dashboard" id="dashboard">
        <div class="card green"><div class="icon">❤️</div><h3>Health</h3><div class="value" id="healthScore">100</div><div class="sub">/100</div></div>
        <div class="card red"><div class="icon">🔴</div><h3>Critical</h3><div class="value" id="criticalErrors">0</div><div class="sub">errors</div></div>
        <div class="card yellow"><div class="icon">🟡</div><h3>Warnings</h3><div class="value" id="warnings">0</div><div class="sub">issues</div></div>
        <div class="card blue"><div class="icon">🔧</div><h3>Fixes</h3><div class="value" id="fixesApplied">0</div><div class="sub">applied</div></div>
        <div class="card purple"><div class="icon">🧠</div><h3>AI Progress</h3><div class="value" id="progressCount">0%</div><div class="sub" id="progressSub">idle</div></div>
        <div class="card cyan"><div class="icon">📊</div><h3>Errors</h3><div class="value" id="totalErrors">0</div><div class="sub">total detected</div></div>
    </div>

    <!-- Progress -->
    <div class="progress-section" id="progressSection">
        <div class="progress-header">
            <span class="progress-title">🧠 <span class="highlight" id="progressTitle">AI Improvising...</span></span>
            <span class="progress-percent" id="progressPercent">0%</span>
        </div>
        <div class="progress-track"><div class="fill" id="progressBar"></div></div>
        <div class="progress-status">
            <span id="progressStatus">Initializing AI engine...</span>
            <span id="progressCountLabel">0 / 0</span>
        </div>
        <div class="progress-details" id="progressDetails">
            <div class="detail-item info">⏳ AI Engine ready. Waiting for commands...</div>
        </div>
    </div>

    <!-- Error Summary -->
    <div class="status-section">
        <h3>📊 Error Summary</h3>
        <div class="error-summary" id="errorSummary">
            <div class="item">🔴 SYSTEMD_FAILURE: <span class="count critical" id="systemdCount">0</span></div>
            <div class="item">🟡 Other Errors: <span class="count warning" id="otherCount">0</span></div>
            <div class="item">📌 Unique Errors: <span class="count info" id="uniqueCount">0</span></div>
            <div class="item">🧠 AI Solutions: <span class="count info" id="aiSolutions">0</span></div>
        </div>
    </div>

    <!-- Status -->
    <div class="status-section">
        <h3>📡 System Status</h3>
        <div id="statusList">
            <div class="status-item">
                <span>🟢 AI Engine Active & Ready</span>
                <span class="status-badge ai">AI Ready</span>
            </div>
        </div>
    </div>

    <!-- Logs -->
    <div class="status-section">
        <h3>📋 Live Logs</h3>
        <div class="logs" id="logs">
            <div class="log-entry ai"><span class="time">[INIT]</span> 🧠 AI Engine initialized. Self-learning mode active.</div>
            <div class="log-entry info"><span class="time">[INIT]</span> 🌐 Internet search engine ready.</div>
            <div class="log-entry info"><span class="time">[INIT]</span> 📚 Learning database loaded.</div>
            <div class="log-entry info"><span class="time">[INIT]</span> ✅ System ready. Click "Scan System" to start.</div>
        </div>
    </div>
</div>

<script>
// =============================================================================
// GLOBALS
// =============================================================================
let isRunning = false;
let isFixing = false;
let eventSource = null;
let fixThreadId = null;

// =============================================================================
// LOGGING
// =============================================================================
function addLog(message, type = 'info') {
    const logs = document.getElementById('logs');
    const entry = document.createElement('div');
    entry.className = `log-entry ${type}`;
    const time = new Date().toLocaleTimeString();
    entry.innerHTML = `<span class="time">[${time}]</span> ${message}`;
    logs.appendChild(entry);
    logs.scrollTop = logs.scrollHeight;
    while (logs.children.length > 300) logs.removeChild(logs.firstChild);
}

function addDetail(message, type = 'info') {
    const details = document.getElementById('progressDetails');
    const entry = document.createElement('div');
    entry.className = `detail-item ${type}`;
    entry.textContent = message;
    details.appendChild(entry);
    details.scrollTop = details.scrollHeight;
    while (details.children.length > 150) details.removeChild(details.firstChild);
}

// =============================================================================
// UI UPDATES
// =============================================================================
function updateDashboard(data) {
    if (!data) return;
    document.getElementById('healthScore').textContent = data.health_score || 100;
    document.getElementById('criticalErrors').textContent = data.critical_errors || 0;
    document.getElementById('warnings').textContent = data.warnings || 0;
    document.getElementById('fixesApplied').textContent = data.fixes_applied || 0;
    document.getElementById('totalErrors').textContent = data.total_errors || 0;
    
    if (data.error_summary) {
        document.getElementById('systemdCount').textContent = data.error_summary.systemd_count || 0;
        document.getElementById('otherCount').textContent = data.error_summary.other_count || 0;
        document.getElementById('uniqueCount').textContent = data.error_summary.unique_count || 0;
        document.getElementById('aiSolutions').textContent = data.error_summary.ai_solutions || 0;
    }
}

function updateProgress(data) {
    const pct = data.percent || 0;
    document.getElementById('progressPercent').textContent = pct + '%';
    document.getElementById('progressBar').style.width = pct + '%';
    document.getElementById('progressCountLabel').textContent = `${data.current || 0} / ${data.total || 0}`;
    document.getElementById('progressStatus').textContent = data.status || 'Processing...';
    document.getElementById('progressCount').textContent = pct + '%';
    document.getElementById('progressSub').textContent = data.status || 'processing';
    
    if (data.current_fix) {
        document.getElementById('progressTitle').textContent = data.current_fix;
    }
    
    if (pct >= 100) {
        document.getElementById('progressBar').className = 'fill complete';
        document.getElementById('progressStatus').textContent = '✅ Complete!';
        document.getElementById('progressSub').textContent = 'complete';
    }
}

function showProgress(show) {
    const section = document.getElementById('progressSection');
    section.className = 'progress-section' + (show ? ' active' : '');
}

function updateStatus(statuses) {
    const list = document.getElementById('statusList');
    list.innerHTML = '';
    statuses.forEach(status => {
        const item = document.createElement('div');
        item.className = 'status-item';
        const badge = document.createElement('span');
        badge.className = `status-badge ${status.status}`;
        badge.textContent = status.status.toUpperCase();
        item.innerHTML = `<span>${status.icon || '•'} ${status.message}</span>`;
        item.appendChild(badge);
        list.appendChild(item);
    });
}

// =============================================================================
// ACTIONS
// =============================================================================
async function runDiagnostic() {
    if (isRunning) return;
    isRunning = true;
    document.getElementById('runBtn').disabled = true;
    document.getElementById('fixBtn').disabled = true;
    document.getElementById('fastBtn').disabled = true;
    addLog('🔍 Starting AI-powered system scan...', 'ai');

    try {
        const response = await fetch('/diagnostic', { method: 'POST' });
        const data = await response.json();
        
        const total = data.summary?.total_errors || 0;
        const systemd = data.error_summary?.systemd_count || 0;
        
        addLog(`✅ Scan complete: ${total} errors found (${systemd} SYSTEMD errors)`, total > 0 ? 'warn' : 'info');
        updateDashboard(data);
        
        if (total > 0) {
            document.getElementById('fixBtn').disabled = false;
            document.getElementById('fastBtn').disabled = false;
            addLog(`🧠 AI Engine ready to fix ${total} errors. Click "AI Fix All" for full fix.`, 'ai');
            updateStatus([
                { icon: '🔴', message: `${total} errors detected (${systemd} SYSTEMD)`, status: 'error' },
                { icon: '🧠', message: `AI Engine has ${data.error_summary?.ai_solutions || 0} known solutions`, status: 'ai' }
            ]);
        } else {
            addLog('🎉 No errors detected! System is healthy.', 'info');
            updateStatus([{ icon: '✅', message: 'System is healthy', status: 'ok' }]);
        }
    } catch (error) {
        addLog(`❌ Error: ${error.message}`, 'error');
    }

    isRunning = false;
    document.getElementById('runBtn').disabled = false;
}

async function runFix() {
    await startFix('full');
}

async function runFixFast() {
    await startFix('fast');
}

async function startFix(mode) {
    if (isFixing) return;
    isFixing = true;
    document.getElementById('fixBtn').disabled = true;
    document.getElementById('fastBtn').disabled = true;
    document.getElementById('runBtn').disabled = true;
    document.getElementById('stopBtn').disabled = false;
    document.getElementById('progressDetails').innerHTML = '';
    showProgress(true);
    addLog(`🧠 AI Engine starting ${mode} fix mode...`, 'ai');
    updateStatus([{ icon: '🧠', message: `AI Fixing (${mode} mode)...`, status: 'running' }]);

    try {
        const response = await fetch('/fix/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mode: mode })
        });
        const data = await response.json();
        fixThreadId = data.thread_id;
        
        addLog(`📋 Fix session started (ID: ${fixThreadId})`, 'info');
        
        if (eventSource) eventSource.close();
        eventSource = new EventSource('/fix/progress?thread_id=' + fixThreadId);
        
        eventSource.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === 'progress') {
                updateProgress(data);
                if (data.current_fix) {
                    addDetail(`🔧 ${data.current_fix}`, 'info');
                }
            } else if (data.type === 'detail') {
                const type = data.success ? 'success' : 'error';
                addDetail(`${data.success ? '✅' : '❌'} ${data.message}`, type);
            } else if (data.type === 'ai') {
                addDetail(`🧠 ${data.message}`, 'ai');
            } else if (data.type === 'complete') {
                addLog(`✅ AI Fix complete: ${data.fixes_applied} fixes applied`, 'info');
                if (data.unresolved > 0) {
                    addLog(`⚠ ${data.unresolved} errors still need manual intervention`, 'warn');
                }
                updateDashboard(data);
                showProgress(false);
                document.getElementById('fixBtn').disabled = true;
                document.getElementById('fastBtn').disabled = true;
                document.getElementById('stopBtn').disabled = true;
                isFixing = false;
                updateStatus([
                    { icon: '✅', message: `AI Fixed ${data.fixes_applied} errors`, status: 'ok' }
                ]);
                if (data.unresolved > 0) {
                    updateStatus([
                        { icon: '⚠', message: `${data.unresolved} errors unresolved`, status: 'warn' }
                    ]);
                }
                eventSource.close();
                eventSource = null;
            } else if (data.type === 'error') {
                addLog(`❌ Error: ${data.message}`, 'error');
            }
        };
        eventSource.onerror = function() {
            addLog('⚠ Progress stream disconnected', 'warn');
        };
    } catch (error) {
        addLog(`❌ Error: ${error.message}`, 'error');
        isFixing = false;
        document.getElementById('fixBtn').disabled = false;
        document.getElementById('fastBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
        showProgress(false);
    }
}

async function stopFix() {
    if (!isFixing || !fixThreadId) return;
    try {
        const response = await fetch('/fix/stop', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ thread_id: fixThreadId })
        });
        const data = await response.json();
        addLog(`⏹ AI Fix stopped: ${data.message || 'by user'}`, 'warn');
        isFixing = false;
        document.getElementById('fixBtn').disabled = false;
        document.getElementById('fastBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
        showProgress(false);
        if (eventSource) { eventSource.close(); eventSource = null; }
        updateStatus([{ icon: '⏹', message: 'Fix stopped by user', status: 'warn' }]);
    } catch (error) {
        addLog(`❌ Error: ${error.message}`, 'error');
    }
}

function clearLogs() {
    document.getElementById('logs').innerHTML = '';
    addLog('🗑 Logs cleared', 'info');
    document.getElementById('progressDetails').innerHTML = '';
    addDetail('⏳ AI Engine ready.', 'info');
}

// =============================================================================
// AUTO-START
// =============================================================================
setTimeout(() => {
    addLog('🚀 Auto-starting diagnostic scan...', 'ai');
    runDiagnostic();
}, 1500);
</script>
</body>
</html>
'''

#===============================================================================
# AI IMPROVISATION ENGINE - FINAL VERSION
#===============================================================================
class ImprovisationEngine:
    """AI-powered improvisation engine with self-learning and internet search"""
    
    def __init__(self):
        self.learning_db = '/var/log/autofixdetect/learning_db.json'
        self.search_cache = '/var/log/autofixdetect/search_cache.json'
        self.successful_fixes = defaultdict(list)
        self.failed_attempts = defaultdict(list)
        self.error_patterns = self._load_patterns()
        self.ai_solutions_count = 0
        self._load_learning_db()
        self._ensure_dirs()
        self._print_ai_status()
        
    def _ensure_dirs(self):
        """Ensure required directories exist"""
        for path in ['/var/log/autofixdetect', '/var/log/autofixdetect/solutions']:
            os.makedirs(path, exist_ok=True)
    
    def _print_ai_status(self):
        """Print AI engine status"""
        print(f"{colors.PURPLE}🧠 AI Engine: Active{colors.NC}")
        print(f"{colors.DIM}   Learning Database: {len(self.successful_fixes)} error patterns learned{colors.NC}")
        print(f"{colors.DIM}   Search Cache: {'Enabled' if os.path.exists(self.search_cache) else 'Empty'}{colors.NC}")
    
    def _load_patterns(self) -> Dict:
        """Load or initialize error patterns with comprehensive database"""
        default_patterns = {
            'systemd_af_vsock': {
                'patterns': [
                    r'Failed to query local AF_VSOCK CID',
                    r'systemd-ssh-generator.*failed',
                    r'AF_VSOCK',
                    r'sd-exec.*failed',
                    r'vsock.*error'
                ],
                'severity': 'critical',
                'category': 'systemd',
                'known_fixes': [
                    'systemctl daemon-reload',
                    'systemctl restart systemd-logind',
                    'systemctl restart systemd-udevd',
                    'systemctl restart systemd-journald',
                    'echo "vsock" > /proc/modules',
                    'systemctl reset-failed'
                ],
                'search_terms': [
                    'AF_VSOCK CID failed systemd fix',
                    'systemd-ssh-generator AF_VSOCK error debian',
                    'Failed to query local AF_VSOCK CID solution',
                    'systemd vsock error fix'
                ]
            },
            'service_timeout': {
                'patterns': [
                    r'Watchdog timeout',
                    r'service.*timeout',
                    r'Timed out',
                    r'Timeout.*service'
                ],
                'severity': 'warning',
                'category': 'systemd',
                'known_fixes': [
                    'systemctl daemon-reload',
                    'systemctl reset-failed',
                    'systemctl restart <service>',
                    'systemctl status <service>'
                ],
                'search_terms': [
                    'systemd watchdog timeout fix',
                    'service timeout systemd solution',
                    'systemd service timeout increase'
                ]
            },
            'service_crashed': {
                'patterns': [
                    r'service.*failed',
                    r'process.*crashed',
                    r'segfault',
                    r'core dumped',
                    r'exited with code'
                ],
                'severity': 'critical',
                'category': 'service',
                'known_fixes': [
                    'systemctl restart <service>',
                    'systemctl reset-failed <service>',
                    'systemctl enable <service>',
                    'journalctl -u <service> -n 50'
                ],
                'search_terms': [
                    'service crashed systemd fix',
                    'systemd service failed restart',
                    'process crashed linux fix'
                ]
            },
            'memory_high': {
                'patterns': [
                    r'Out of memory',
                    r'oom-killer',
                    r'Memory usage',
                    r'high memory'
                ],
                'severity': 'warning',
                'category': 'memory',
                'known_fixes': [
                    'echo 3 > /proc/sys/vm/drop_caches',
                    'swapoff -a && swapon -a',
                    'free -h && ps aux --sort=-%mem | head -10'
                ],
                'search_terms': [
                    'linux high memory usage fix',
                    'oom killer solution',
                    'clear cache memory linux'
                ]
            },
            'disk_full': {
                'patterns': [
                    r'No space left on device',
                    r'disk full',
                    r'ENOSPC',
                    r'not enough free space'
                ],
                'severity': 'critical',
                'category': 'disk',
                'known_fixes': [
                    'apt-get clean',
                    'apt-get autoremove -y',
                    'journalctl --vacuum-size=100M',
                    'find /tmp -type f -mtime +7 -delete'
                ],
                'search_terms': [
                    'linux disk full fix',
                    'no space left on device solution',
                    'clean disk space linux'
                ]
            },
            'network_error': {
                'patterns': [
                    r'connection timed out',
                    r'network.*failed',
                    r'Cannot connect',
                    r'Network is unreachable'
                ],
                'severity': 'warning',
                'category': 'network',
                'known_fixes': [
                    'systemctl restart networking',
                    'systemctl restart NetworkManager',
                    'ip link set <interface> down && up',
                    'systemctl restart systemd-resolved'
                ],
                'search_terms': [
                    'linux network connection timeout fix',
                    'network unreachable solution',
                    'restart networking linux'
                ]
            },
            'package_error': {
                'patterns': [
                    r'broken package',
                    r'unmet dependencies',
                    r'dpkg.*error',
                    r'package.*failed'
                ],
                'severity': 'critical',
                'category': 'package',
                'known_fixes': [
                    'apt-get install -f -y',
                    'apt-get update && apt-get upgrade -y',
                    'dpkg --configure -a'
                ],
                'search_terms': [
                    'apt broken package fix',
                    'unmet dependencies solution',
                    'dpkg error fix'
                ]
            }
        }
        
        pattern_file = '/var/log/autofixdetect/error_patterns.json'
        if os.path.exists(pattern_file):
            try:
                with open(pattern_file, 'r') as f:
                    loaded = json.load(f)
                    default_patterns.update(loaded)
                    return default_patterns
            except:
                pass
        
        with open(pattern_file, 'w') as f:
            json.dump(default_patterns, f, indent=2)
        
        return default_patterns
    
    def _load_learning_db(self):
        """Load learning database"""
        if os.path.exists(self.learning_db):
            try:
                with open(self.learning_db, 'r') as f:
                    data = json.load(f)
                    self.successful_fixes = defaultdict(list, data.get('successful', {}))
                    self.failed_attempts = defaultdict(list, data.get('failed', {}))
                    self.ai_solutions_count = data.get('ai_solutions_count', 0)
                    return
            except:
                pass
        
        self.successful_fixes = defaultdict(list)
        self.failed_attempts = defaultdict(list)
        self.ai_solutions_count = 0
        self._save_learning_db()
    
    def _save_learning_db(self):
        """Save learning database"""
        try:
            with open(self.learning_db, 'w') as f:
                json.dump({
                    'successful': dict(self.successful_fixes),
                    'failed': dict(self.failed_attempts),
                    'ai_solutions_count': self.ai_solutions_count,
                    'last_updated': datetime.now().isoformat()
                }, f, indent=2)
        except:
            pass
    
    def search_internet(self, query: str) -> List[Dict]:
        """Search internet for solutions"""
        results = []
        cache_key = hashlib.md5(query.encode()).hexdigest()
        
        # Check cache
        if os.path.exists(self.search_cache):
            try:
                with open(self.search_cache, 'r') as f:
                    cache = json.load(f)
                    if cache_key in cache:
                        return cache[cache_key]
            except:
                pass
        
        print(f"{colors.YELLOW}🔍 Searching internet: {query[:50]}...{colors.NC}")
        
        # Try multiple sources
        sources = [
            self._search_stackoverflow,
            self._search_github,
            self._search_duckduckgo,
            self._search_linux_forums
        ]
        
        for source in sources:
            try:
                source_results = source(query)
                if source_results:
                    results.extend(source_results)
                    break
            except:
                continue
        
        # Cache results
        if results:
            try:
                cache = {}
                if os.path.exists(self.search_cache):
                    with open(self.search_cache, 'r') as f:
                        cache = json.load(f)
                cache[cache_key] = results
                with open(self.search_cache, 'w') as f:
                    json.dump(cache, f, indent=2)
            except:
                pass
        
        return results
    
    def _search_stackoverflow(self, query: str) -> List[Dict]:
        """Search Stack Overflow API"""
        results = []
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            encoded = urllib.parse.quote(query)
            url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={encoded}&site=stackoverflow&pagesize=5"
            
            req = urllib.request.Request(url, headers={'User-Agent': 'AutoFixDetect/10.0'})
            response = urllib.request.urlopen(req, timeout=8, context=ctx)
            data = json.loads(response.read().decode())
            
            if 'items' in data:
                for item in data['items'][:5]:
                    results.append({
                        'source': 'Stack Overflow',
                        'title': item.get('title', ''),
                        'link': item.get('link', ''),
                        'score': item.get('score', 0),
                        'solution': item.get('body', '')[:500] if 'body' in item else ''
                    })
        except:
            pass
        return results
    
    def _search_github(self, query: str) -> List[Dict]:
        """Search GitHub Issues"""
        results = []
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            encoded = urllib.parse.quote(query)
            url = f"https://api.github.com/search/issues?q={encoded}+state:closed&per_page=5"
            
            req = urllib.request.Request(url, headers={'User-Agent': 'AutoFixDetect/10.0'})
            response = urllib.request.urlopen(req, timeout=8, context=ctx)
            data = json.loads(response.read().decode())
            
            if 'items' in data:
                for item in data['items'][:5]:
                    results.append({
                        'source': 'GitHub',
                        'title': item.get('title', ''),
                        'link': item.get('html_url', ''),
                        'solution': item.get('body', '')[:500] if 'body' in item else ''
                    })
        except:
            pass
        return results
    
    def _search_duckduckgo(self, query: str) -> List[Dict]:
        """Search DuckDuckGo"""
        results = []
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            encoded = urllib.parse.quote(query)
            url = f"https://html.duckduckgo.com/html/?q={encoded}"
            
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=8, context=ctx)
            html = response.read().decode('utf-8', errors='ignore')
            
            links = re.findall(r'<a[^>]*href="([^"]*)"[^>]*class="result__a"[^>]*>(.*?)</a>', html)
            for link, title in links[:5]:
                title_clean = re.sub(r'<[^>]+>', '', title)
                results.append({
                    'source': 'DuckDuckGo',
                    'title': title_clean,
                    'link': link,
                    'solution': ''
                })
        except:
            pass
        return results
    
    def _search_linux_forums(self, query: str) -> List[Dict]:
        """Search Linux forums"""
        results = []
        forums = [
            ('AskUbuntu', 'https://askubuntu.com'),
            ('UnixSE', 'https://unix.stackexchange.com'),
            ('ServerFault', 'https://serverfault.com')
        ]
        
        for name, url in forums:
            encoded = urllib.parse.quote(query)
            results.append({
                'source': name,
                'title': f'Search: {query[:50]}...',
                'link': f"{url}/search?q={encoded}",
                'solution': ''
            })
        
        return results
    
    def extract_commands(self, solutions: List[Dict]) -> List[str]:
        """Extract shell commands from solution texts"""
        commands = []
        cmd_patterns = [
            r'`([^`]+)`',
            r'```\s*([^`]+)\s*```',
            r'\b(systemctl|apt|yum|dnf|pip|python|journalctl|echo|cat|grep|find|sed|awk|service|update-rc|dpkg|kill|pkill|netstat|ip|ifconfig|route|mount|umount|chmod|chown)\s+[^\n;]+(?:;|$)',
            r'sudo\s+[^\n;]+(?:;|$)',
            r'echo\s+[^>]+>\s*[^\s]+'
        ]
        
        for solution in solutions:
            text = solution.get('title', '') + ' ' + solution.get('solution', '')
            
            for pattern in cmd_patterns:
                matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[0] if match else ''
                    if match and len(match) > 4:
                        # Clean and validate
                        clean_cmd = match.strip()
                        if any(key in clean_cmd for key in ['systemctl', 'apt', 'service', 'journalctl', 'echo', 'ip', 'netstat']):
                            commands.append(clean_cmd[:200])
        
        # Remove duplicates
        seen = set()
        unique = []
        for cmd in commands:
            if cmd and cmd not in seen and len(cmd) > 5:
                seen.add(cmd)
                unique.append(cmd)
        
        return unique[:15]
    
    def improvise_fix(self, error_id: str, error_message: str, error_context: Dict = None) -> List[str]:
        """Improvise a fix using multiple strategies"""
        fixes = []
        
        # Strategy 1: Check learning database
        if error_id in self.successful_fixes:
            learned = self.successful_fixes[error_id]
            if learned:
                fixes.extend(learned[-5:])  # Last 5 successful fixes
                print(f"{colors.DIM}   📚 Found {len(learned)} learned solutions{colors.NC}")
        
        # Strategy 2: Check pattern database
        for pattern_id, pattern in self.error_patterns.items():
            for p in pattern.get('patterns', []):
                if re.search(p, error_message, re.IGNORECASE):
                    known = pattern.get('known_fixes', [])
                    fixes.extend(known)
                    print(f"{colors.DIM}   📋 Found {len(known)} pattern-based solutions{colors.NC}")
                    break
        
        # Strategy 3: Search internet
        search_terms = []
        for pattern_id, pattern in self.error_patterns.items():
            for p in pattern.get('patterns', []):
                if re.search(p, error_message, re.IGNORECASE):
                    search_terms.extend(pattern.get('search_terms', []))
                    break
        
        if not search_terms:
            words = re.findall(r'[A-Za-z_]+', error_message)[:5]
            search_terms.append(' '.join(words) + ' linux fix')
            search_terms.append(error_id + ' error fix')
        
        for term in search_terms[:3]:
            print(f"{colors.DIM}   🌐 Searching: {term[:40]}...{colors.NC}")
            solutions = self.search_internet(term)
            if solutions:
                cmd_fixes = self.extract_commands(solutions)
                fixes.extend(cmd_fixes)
                print(f"{colors.DIM}   🌐 Found {len(cmd_fixes)} commands from {solutions[0].get('source', 'web')}{colors.NC}")
                break
        
        # Strategy 4: Generic fallback fixes
        generic_fixes = [
            'systemctl daemon-reload',
            'systemctl reset-failed',
            'journalctl -p err -b --no-pager | tail -50',
            'systemctl list-units --failed'
        ]
        
        if not fixes:
            fixes.extend(generic_fixes)
            print(f"{colors.DIM}   🔧 Using generic fallback fixes{colors.NC}")
        
        # Remove duplicates and clean
        seen = set()
        unique = []
        for fix in fixes:
            if fix and fix not in seen and len(fix) > 3:
                seen.add(fix)
                unique.append(fix)
        
        return unique[:15]
    
    def try_fix(self, command: str, context: Dict = None) -> Dict:
        """Try a fix command and return result"""
        result = {
            'command': command[:100],
            'success': False,
            'output': '',
            'error': ''
        }
        
        try:
            print(f"{colors.WHITE}  🔧 Trying: {command[:70]}...{colors.NC}")
            
            proc = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            result['output'] = proc.stdout[:300] if proc.stdout else ''
            result['error'] = proc.stderr[:300] if proc.stderr else ''
            result['success'] = proc.returncode == 0
            
            if result['success']:
                print(f"{colors.GREEN}    ✅ Success{colors.NC}")
                if context:
                    self._record_success(context.get('error_id', 'unknown'), command)
            else:
                print(f"{colors.RED}    ❌ Failed (code: {proc.returncode}){colors.NC}")
                if context:
                    self._record_failure(context.get('error_id', 'unknown'), command)
                    
        except subprocess.TimeoutExpired:
            result['error'] = 'Timeout after 30s'
            print(f"{colors.RED}    ❌ Timeout{colors.NC}")
        except Exception as e:
            result['error'] = str(e)
            print(f"{colors.RED}    ❌ Error: {str(e)[:50]}{colors.NC}")
        
        return result
    
    def _record_success(self, error_id: str, command: str):
        """Record a successful fix"""
        self.successful_fixes[error_id].append({
            'command': command,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.successful_fixes[error_id]) > 20:
            self.successful_fixes[error_id] = self.successful_fixes[error_id][-20:]
        self.ai_solutions_count += 1
        self._save_learning_db()
    
    def _record_failure(self, error_id: str, command: str):
        """Record a failed fix attempt"""
        self.failed_attempts[error_id].append({
            'command': command,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.failed_attempts[error_id]) > 20:
            self.failed_attempts[error_id] = self.failed_attempts[error_id][-20:]
        self._save_learning_db()
    
    def smart_fix(self, error: Dict, progress_callback=None) -> Dict:
        """Smart fix with improvisation and learning"""
        error_id = error.get('error_id', 'UNKNOWN')
        error_message = error.get('message', '')
        
        if progress_callback:
            progress_callback('ai', f"🧠 AI analyzing: {error_id}")
        
        print(f"\n{colors.PURPLE}🧠 AI Improvising: {error_id}{colors.NC}")
        print(f"{colors.DIM}   Message: {error_message[:80]}{colors.NC}")
        
        fixes = self.improvise_fix(error_id, error_message, error)
        
        if not fixes:
            return {
                'error_id': error_id,
                'success': False,
                'message': 'No solution found',
                'attempted_commands': [],
                'successful_commands': []
            }
        
        print(f"{colors.YELLOW}📋 Testing {len(fixes)} solutions{colors.NC}")
        
        attempted = []
        successful = []
        
        for i, fix_cmd in enumerate(fixes[:15], 1):
            if progress_callback:
                progress_callback('detail', f"[{i}/{min(len(fixes), 15)}] {fix_cmd[:50]}...")
            
            result = self.try_fix(fix_cmd, {'error_id': error_id})
            attempted.append(fix_cmd)
            
            if result['success']:
                successful.append(fix_cmd)
                if progress_callback:
                    progress_callback('success', f"✅ {fix_cmd[:50]}...")
                if len(successful) >= 2:  # Stop after 2 successful commands
                    break
            else:
                if progress_callback:
                    progress_callback('error', f"❌ {fix_cmd[:50]}...")
        
        return {
            'error_id': error_id,
            'success': len(successful) > 0,
            'message': f"Found {len(successful)} working solutions",
            'attempted_commands': attempted[:10],
            'successful_commands': successful[:5]
        }
    
    def get_error_summary(self, errors: List[Dict]) -> Dict:
        """Generate error summary with AI statistics"""
        systemd_count = 0
        other_count = 0
        unique_errors = set()
        
        for error in errors:
            err_id = error.get('error_id', 'UNKNOWN')
            unique_errors.add(err_id)
            if 'SYSTEMD' in err_id or 'systemd' in error.get('message', '').lower():
                systemd_count += 1
            else:
                other_count += 1
        
        return {
            'systemd_count': systemd_count,
            'other_count': other_count,
            'unique_count': len(unique_errors),
            'ai_solutions': self.ai_solutions_count
        }

#===============================================================================
# PROGRESS TRACKER
#===============================================================================
class ProgressTracker:
    """Track progress of fix operations"""
    
    def __init__(self):
        self.threads = {}
        self.lock = threading.Lock()
    
    def create(self, thread_id: str, total: int) -> Dict:
        with self.lock:
            self.threads[thread_id] = {
                'id': thread_id,
                'total': total,
                'current': 0,
                'percent': 0,
                'status': 'running',
                'current_fix': 'Initializing AI...',
                'details': [],
                'start_time': datetime.now().isoformat()
            }
            return self.threads[thread_id]
    
    def update(self, thread_id: str, current: int, current_fix: str = None, detail: str = None, detail_type: str = 'info'):
        with self.lock:
            if thread_id not in self.threads:
                return
            thread = self.threads[thread_id]
            thread['current'] = current
            thread['percent'] = int((current / thread['total']) * 100) if thread['total'] > 0 else 0
            if current_fix:
                thread['current_fix'] = current_fix
            if detail:
                thread['details'].append({
                    'timestamp': datetime.now().isoformat(),
                    'message': detail,
                    'type': detail_type
                })
    
    def complete(self, thread_id: str, results: Dict):
        with self.lock:
            if thread_id in self.threads:
                self.threads[thread_id]['status'] = 'complete'
                self.threads[thread_id]['results'] = results
    
    def get(self, thread_id: str) -> Optional[Dict]:
        with self.lock:
            return self.threads.get(thread_id)
    
    def stop(self, thread_id: str):
        with self.lock:
            if thread_id in self.threads:
                self.threads[thread_id]['status'] = 'stopped'

#===============================================================================
# HTTP SERVER WITH SSE
#===============================================================================
class HTTPServer:
    """HTTP server with SSE for real-time updates"""
    
    def __init__(self, port=8080):
        self.port = port
        self.server = None
        self.engine = None
        self.progress = ProgressTracker()
        self.fix_threads = {}
    
    def set_engine(self, engine):
        self.engine = engine
    
    def start(self):
        try:
            import http.server
            import socketserver
            
            class Handler(http.server.BaseHTTPRequestHandler):
                def do_GET(self):
                    if self.path == '/':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html; charset=utf-8')
                        self.end_headers()
                        self.wfile.write(WEB_UI_HTML.encode('utf-8'))
                    
                    elif self.path.startswith('/fix/progress'):
                        self.send_response(200)
                        self.send_header('Content-Type', 'text/event-stream')
                        self.send_header('Cache-Control', 'no-cache')
                        self.send_header('Connection', 'keep-alive')
                        self.end_headers()
                        
                        thread_id = None
                        if '?' in self.path:
                            for p in self.path.split('?')[1].split('&'):
                                if p.startswith('thread_id='):
                                    thread_id = p.split('=')[1]
                        
                        if not thread_id:
                            return
                        
                        last_pct = -1
                        sent_details = 0
                        
                        while True:
                            progress = self.server.progress.get(thread_id)
                            if not progress:
                                break
                            
                            # Send progress update
                            if progress['percent'] != last_pct:
                                last_pct = progress['percent']
                                data = {
                                    'type': 'progress',
                                    'percent': progress['percent'],
                                    'current': progress['current'],
                                    'total': progress['total'],
                                    'status': progress['status'],
                                    'current_fix': progress.get('current_fix', '')
                                }
                                self.wfile.write(b"data: " + json.dumps(data).encode() + b"\n\n")
                                self.wfile.flush()
                            
                            # Send details
                            details = progress.get('details', [])
                            if details:
                                for detail in details[sent_details:]:
                                    detail_type = detail.get('type', 'info')
                                    data = {
                                        'type': 'detail' if detail_type != 'ai' else 'ai',
                                        'message': detail.get('message', ''),
                                        'success': detail_type == 'success'
                                    }
                                    self.wfile.write(b"data: " + json.dumps(data).encode() + b"\n\n")
                                    self.wfile.flush()
                                    sent_details += 1
                                progress['details'] = []
                            
                            if progress['status'] == 'complete':
                                results = progress.get('results', {})
                                data = {
                                    'type': 'complete',
                                    'fixes_applied': results.get('fixes_applied', 0),
                                    'unresolved': results.get('unresolved', 0),
                                    'health_score': results.get('health_score', 100)
                                }
                                self.wfile.write(b"data: " + json.dumps(data).encode() + b"\n\n")
                                self.wfile.flush()
                                break
                            
                            if progress['status'] == 'stopped':
                                self.wfile.write(b"data: " + json.dumps({'type': 'stopped'}).encode() + b"\n\n")
                                self.wfile.flush()
                                break
                            
                            time.sleep(0.5)
                    
                    else:
                        self.send_response(404)
                        self.end_headers()
                
                def do_POST(self):
                    if self.path == '/diagnostic':
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        if self.server.engine:
                            results = self.server.engine.run_diagnostic()
                            self.wfile.write(json.dumps(results).encode())
                    
                    elif self.path == '/fix/start':
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        
                        thread_id = str(uuid.uuid4())[:8]
                        errors = self.server.engine.errors if self.server.engine else []
                        total = len(errors)
                        
                        if total == 0:
                            self.wfile.write(json.dumps({'thread_id': thread_id, 'status': 'no_errors'}).encode())
                            return
                        
                        self.server.progress.create(thread_id, total)
                        
                        def run_ai_fixes():
                            try:
                                progress = self.server.progress
                                improvisor = self.server.engine.improvisor if self.server.engine else None
                                applied = 0
                                unresolved = 0
                                errors = self.server.engine.errors
                                error_summary = improvisor.get_error_summary(errors) if improvisor else {}
                                
                                progress.update(thread_id, 0, "🧠 AI Engine Starting", "🧠 AI Improvisation Engine active", 'ai')
                                
                                for i, error in enumerate(errors):
                                    thread_data = progress.get(thread_id)
                                    if thread_data and thread_data['status'] == 'stopped':
                                        break
                                    
                                    error_id = error.get('error_id', 'UNKNOWN')
                                    progress.update(thread_id, i, f"🧠 AI: {error_id}")
                                    
                                    if improvisor:
                                        result = improvisor.smart_fix(error, 
                                            lambda t, m: progress.update(thread_id, i, f"🧠 {error_id}", m, 'ai' if t == 'ai' else 'info')
                                        )
                                        
                                        if result.get('success', False):
                                            applied += 1
                                            progress.update(thread_id, i, f"✅ {error_id} fixed", f"✅ AI fixed {error_id}", 'success')
                                        else:
                                            unresolved += 1
                                            progress.update(thread_id, i, f"❌ {error_id}", f"❌ Could not fix {error_id}", 'error')
                                    else:
                                        unresolved += 1
                                
                                # Calculate health score
                                health_score = max(0, 100 - unresolved * 10)
                                
                                results = {
                                    'fixes_applied': applied,
                                    'unresolved': unresolved,
                                    'health_score': health_score,
                                    'error_summary': error_summary
                                }
                                progress.complete(thread_id, results)
                                
                            except Exception as e:
                                progress.update(thread_id, 0, f"Error: {str(e)}", f"❌ AI Error: {str(e)}", 'error')
                                progress.complete(thread_id, {'error': str(e)})
                        
                        thread = threading.Thread(target=run_ai_fixes, daemon=True)
                        thread.start()
                        self.server.fix_threads[thread_id] = thread
                        
                        self.wfile.write(json.dumps({'thread_id': thread_id, 'status': 'started'}).encode())
                    
                    elif self.path == '/fix/stop':
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        
                        content_length = int(self.headers.get('Content-Length', 0))
                        body = self.rfile.read(content_length).decode() if content_length > 0 else '{}'
                        data = json.loads(body) if body else {}
                        thread_id = data.get('thread_id')
                        
                        if thread_id:
                            self.server.progress.stop(thread_id)
                            self.wfile.write(json.dumps({'message': 'Stopped by user'}).encode())
                        else:
                            self.wfile.write(json.dumps({'error': 'No thread_id'}).encode())
                    
                    else:
                        self.send_response(404)
                        self.end_headers()
                
                def log_message(self, fmt, *args):
                    pass
            
            self.server = socketserver.TCPServer(("0.0.0.0", self.port), Handler)
            self.server.progress = self.progress
            self.server.engine = self.engine
            self.server.fix_threads = self.fix_threads
            
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            return True
        except Exception as e:
            print(f"{colors.RED}Failed to start web server: {e}{colors.NC}")
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()

#===============================================================================
# SYSTEM INFO
#===============================================================================
class SystemInfo:
    """System information collector"""
    
    @staticmethod
    def get_cpu_count() -> int:
        try:
            return os.cpu_count() or 1
        except:
            return 1
    
    @staticmethod
    def get_memory_info() -> Dict:
        try:
            with open('/proc/meminfo', 'r') as f:
                mem = {}
                for line in f:
                    parts = line.split(':')
                    if len(parts) == 2:
                        mem[parts[0].strip()] = int(parts[1].strip().split()[0])
                
                total = mem.get('MemTotal', 0)
                avail = mem.get('MemAvailable', 0)
                used = total - avail
                pct = (used / total * 100) if total > 0 else 0
                return {'total': total * 1024, 'used': used * 1024, 'percent': round(pct, 2)}
        except:
            return {'total': 0, 'used': 0, 'percent': 0}
    
    @staticmethod
    def get_disk_usage(path: str = '/') -> Dict:
        try:
            stat = os.statvfs(path)
            total = stat.f_blocks * stat.f_frsize
            free = stat.f_bfree * stat.f_frsize
            used = total - free
            pct = (used / total * 100) if total > 0 else 0
            return {'total': total, 'used': used, 'percent': round(pct, 2)}
        except:
            return {'total': 0, 'used': 0, 'percent': 0}
    
    @staticmethod
    def get_uptime() -> str:
        try:
            with open('/proc/uptime', 'r') as f:
                sec = float(f.readline().split()[0])
                d = int(sec // 86400)
                h = int((sec % 86400) // 3600)
                m = int((sec % 3600) // 60)
                if d > 0:
                    return f"{d}d {h}h {m}m"
                elif h > 0:
                    return f"{h}h {m}m"
                return f"{m}m"
        except:
            return "Unknown"

#===============================================================================
# ERROR DETECTOR
#===============================================================================
class ErrorDetector:
    """Error detection from logs"""
    
    def __init__(self):
        self.patterns = {
            'SYSTEMD_FAILURE': {
                'patterns': [
                    r'Failed to query local AF_VSOCK CID',
                    r'systemd-ssh-generator.*failed',
                    r'sd-exec.*failed',
                    r'vsock.*error'
                ],
                'severity': 'critical'
            },
            'SERVICE_CRASHED': {
                'patterns': [
                    r'service.*failed',
                    r'process.*crashed',
                    r'segfault',
                    r'core dumped'
                ],
                'severity': 'critical'
            },
            'SERVICE_TIMEOUT': {
                'patterns': [
                    r'Watchdog timeout',
                    r'Timed out',
                    r'service.*timeout'
                ],
                'severity': 'warning'
            },
            'MEMORY_HIGH': {
                'patterns': [
                    r'Out of memory',
                    r'oom-killer',
                    r'memory.*high'
                ],
                'severity': 'warning'
            },
            'DISK_FULL': {
                'patterns': [
                    r'No space left',
                    r'disk full',
                    r'ENOSPC'
                ],
                'severity': 'critical'
            },
            'NETWORK_ERROR': {
                'patterns': [
                    r'connection timed out',
                    r'network.*failed',
                    r'Cannot connect'
                ],
                'severity': 'warning'
            },
            'PACKAGE_ERROR': {
                'patterns': [
                    r'broken package',
                    r'unmet dependencies',
                    r'dpkg.*error'
                ],
                'severity': 'critical'
            }
        }
    
    def detect(self, line: str) -> Optional[Dict]:
        """Detect error in log line"""
        for err_id, info in self.patterns.items():
            for pattern in info['patterns']:
                if re.search(pattern, line, re.IGNORECASE):
                    return {
                        'error_id': err_id,
                        'severity': info['severity'],
                        'message': line.strip()
                    }
        return None

#===============================================================================
# DIAGNOSTIC ENGINE
#===============================================================================
class DiagnosticEngine:
    """Main diagnostic engine with AI improvisation"""
    
    def __init__(self):
        self.errors = []
        self.fixes_applied = 0
        self.health_score = 100
        self.detector = ErrorDetector()
        self.improvisor = ImprovisationEngine()
    
    def run_diagnostic(self) -> Dict:
        """Run full diagnostic"""
        self.errors = []
        self.health_score = 100
        
        print(f"{colors.YELLOW}🔍 Running diagnostic scan...{colors.NC}")
        
        # Check logs
        self._check_logs()
        
        # Check services
        self._check_services()
        
        # Check resources
        self._check_resources()
        
        # Calculate scores
        critical = len([e for e in self.errors if e.get('severity') == 'critical'])
        warnings = len([e for e in self.errors if e.get('severity') == 'warning'])
        self.health_score = max(0, 100 - critical * 10 - warnings * 3)
        
        # Get error summary from AI
        error_summary = self.improvisor.get_error_summary(self.errors)
        
        print(f"{colors.GREEN}✅ Scan complete: {len(self.errors)} errors found{colors.NC}")
        print(f"{colors.DIM}   Critical: {critical}, Warnings: {warnings}{colors.NC}")
        print(f"{colors.DIM}   SYSTEMD errors: {error_summary['systemd_count']}{colors.NC}")
        print(f"{colors.PURPLE}🧠 AI has {error_summary['ai_solutions']} learned solutions{colors.NC}")
        
        return {
            'errors': self.errors,
            'summary': {
                'total_errors': len(self.errors),
                'critical_errors': critical,
                'warnings': warnings,
                'health_score': self.health_score
            },
            'error_summary': error_summary,
            'fixes_applied': self.fixes_applied
        }
    
    def _check_logs(self):
        """Check system logs for errors"""
        log_files = ['/var/log/syslog', '/var/log/messages', '/var/log/kern.log']
        for log_file in log_files:
            if os.path.exists(log_file):
                try:
                    with open(log_file, 'r', errors='ignore') as f:
                        for line in f.readlines()[-500:]:
                            err = self.detector.detect(line)
                            if err:
                                self.errors.append(err)
                except:
                    pass
        
        if shutil.which('journalctl'):
            try:
                result = subprocess.run(
                    ['journalctl', '-p', 'err', '-b', '--no-pager', '-n', '300'],
                    capture_output=True, text=True, timeout=10, check=False
                )
                for line in result.stdout.split('\n'):
                    err = self.detector.detect(line)
                    if err:
                        self.errors.append(err)
            except:
                pass
    
    def _check_services(self):
        """Check system services"""
        if shutil.which('systemctl'):
            try:
                result = subprocess.run(
                    ['systemctl', '--failed', '--no-pager'],
                    capture_output=True, text=True, timeout=5, check=False
                )
                for line in result.stdout.split('\n'):
                    if '.service' in line and '●' not in line and line.strip():
                        parts = line.split()
                        if parts:
                            self.errors.append({
                                'error_id': 'SERVICE_CRASHED',
                                'severity': 'critical',
                                'message': f'Service {parts[0]} failed',
                                'service': parts[0]
                            })
            except:
                pass
    
    def _check_resources(self):
        """Check system resources"""
        mem = SystemInfo.get_memory_info()
        if mem.get('percent', 0) > 90:
            self.errors.append({
                'error_id': 'MEMORY_HIGH',
                'severity': 'warning',
                'message': f'Memory usage: {mem["percent"]}%'
            })
        
        disk = SystemInfo.get_disk_usage('/')
        if disk.get('percent', 0) > 90:
            self.errors.append({
                'error_id': 'DISK_FULL',
                'severity': 'critical',
                'message': f'Disk usage: {disk["percent"]}%'
            })

#===============================================================================
# MAIN APPLICATION
#===============================================================================
class AutoFixDetectAI:
    """Main application with web interface and CLI"""
    
    def __init__(self):
        self.colors = colors
        self.engine = DiagnosticEngine()
        self.web_server = None
        self.start_time = datetime.now()
    
    def print_banner(self):
        """Print banner"""
        print(f"""
{self.colors.CYAN}{self.colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           AUTOFIXDETECT AI v{VERSION} - {VERSION_NAME}              ║
║                                                                            ║
║   ⚡ AI-Powered System Diagnostic & Auto-Fix Tool                          ║
║   🧠 Self-Learning with Internet Search & Improvisation                   ║
║   🌐 Full Web Interface with Real-Time Progress                           ║
║   📚 No External Dependencies - Fully Self-Contained                      ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
{self.colors.NC}
{self.colors.WHITE}📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{self.colors.NC}
{self.colors.DIM}🖥️  {socket.gethostname()} | {SystemInfo.get_cpu_count()} cores | {SystemInfo.get_uptime()} uptime{self.colors.NC}
{self.colors.DIM}🐍 Python {sys.version.split()[0]} | {platform.platform()}{self.colors.NC}
{self.colors.PURPLE}🧠 AI Engine: Active | Self-Learning: Enabled{self.colors.NC}
""")
    
    def start_web(self):
        """Start web interface"""
        self.web_server = HTTPServer(8080)
        self.web_server.set_engine(self.engine)
        if self.web_server.start():
            print(f"{self.colors.GREEN}🌐 Web interface: http://localhost:8080{self.colors.NC}")
            print(f"{self.colors.PURPLE}🧠 AI Improvisation Engine active{self.colors.NC}")
            print(f"{self.colors.GREEN}   Press Ctrl+C to stop{self.colors.NC}")
            return True
        return False
    
    def run_cli(self):
        """Run CLI mode"""
        self.print_banner()
        
        print(f"{self.colors.YELLOW}🔍 Running AI-powered diagnostic...{self.colors.NC}")
        results = self.engine.run_diagnostic()
        summary = results['summary']
        error_summary = results.get('error_summary', {})
        
        print(f"\n{self.colors.WHITE}{self.colors.BOLD}📊 Results:{self.colors.NC}")
        print(f"  ❤️  Health: {summary['health_score']}/100")
        print(f"  📌 Total Errors: {summary['total_errors']}")
        print(f"  🔴 Critical: {summary['critical_errors']}")
        print(f"  🟡 Warnings: {summary['warnings']}")
        print(f"  📚 SYSTEMD Errors: {error_summary.get('systemd_count', 0)}")
        print(f"  🧠 AI Solutions: {error_summary.get('ai_solutions', 0)}")
        
        if results['errors']:
            print(f"\n{self.colors.RED}📋 Error Details:{self.colors.NC}")
            for i, e in enumerate(results['errors'][:10], 1):
                severity = e.get('severity', 'unknown')
                color = self.colors.RED if severity == 'critical' else self.colors.YELLOW
                print(f"  {i}. {color}[{severity.upper()}]{self.colors.NC} {e.get('error_id', 'UNKNOWN')}")
                print(f"     {self.colors.DIM}{e.get('message', '')[:80]}{self.colors.NC}")
            
            if len(results['errors']) > 10:
                print(f"  {self.colors.DIM}... and {len(results['errors']) - 10} more errors{self.colors.NC}")
            
            print(f"\n{self.colors.PURPLE}🧠 AI Engine ready to improvise solutions...{self.colors.NC}")
            resp = input(f"\n{self.colors.WHITE}Run AI fixes? (y/n): {self.colors.NC}")
            
            if resp.lower() in ['y', 'yes']:
                print(f"\n{self.colors.YELLOW}🧠 AI Improvising...{self.colors.NC}")
                fixed = 0
                for error in results['errors']:
                    result = self.engine.improvisor.smart_fix(error)
                    if result['success']:
                        fixed += 1
                        print(f"{self.colors.GREEN}✅ {result['error_id']} fixed{self.colors.NC}")
                    else:
                        print(f"{self.colors.RED}❌ {result['error_id']} unresolved{self.colors.NC}")
                
                print(f"\n{self.colors.GREEN}✅ AI fixed {fixed}/{len(results['errors'])} errors{self.colors.NC}")
                if fixed < len(results['errors']):
                    print(f"{self.colors.YELLOW}⚠ {len(results['errors']) - fixed} errors still need manual intervention{self.colors.NC}")
        else:
            print(f"\n{self.colors.GREEN}🎉 No errors detected! System is healthy.{self.colors.NC}")
    
    def run(self):
        """Run application"""
        if '--web' in sys.argv or '-w' in sys.argv:
            self.print_banner()
            if self.start_web():
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print(f"\n{self.colors.YELLOW}⏹ Shutting down web interface...{self.colors.NC}")
                    if self.web_server:
                        self.web_server.stop()
                    print(f"{self.colors.GREEN}✅ Done.{self.colors.NC}")
            else:
                print(f"{self.colors.RED}Failed to start web interface.{self.colors.NC}")
                self.run_cli()
        else:
            self.run_cli()

#===============================================================================
# ENTRY POINT
#===============================================================================
if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 6):
        print("Python 3.6+ required.")
        sys.exit(1)
    
    # Handle Ctrl+C
    def signal_handler(sig, frame):
        print(f"\n{colors.YELLOW}⏹ Interrupted by user.{colors.NC}")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # Run application
    app = AutoFixDetectAI()
    app.run()
