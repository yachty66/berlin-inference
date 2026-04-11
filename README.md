# Berlin Inference

EU-resident LLM inference for OpenRouter. Based in Berlin, served from Frankfurt.

## Why

OpenRouter offers EU in-region routing (`eu.openrouter.ai`) to enterprise customers
who need prompts and completions to stay inside the EU — GDPR, the EU AI Act, and
Schrems II make this a hard requirement for fintech, health, and public-sector
buyers. But the EU-routable catalog is thin: many open-weight models on OpenRouter
are served by a single global provider, and that provider is often hosted in APAC
or the US. For EU enterprise, those models are listed but not legally consumable.

Berlin Inference plugs that gap. We run popular open-weight models on professional
GPU infrastructure in Frankfurt, with a German legal entity and a DPA-ready posture,
and list them on OpenRouter as a second (or first) EU source.

## Launch model

**`qwen/qwq-32b`** — Alibaba's 32B reasoning model, Apache 2.0.

- Fits on a single H100 80GB (bf16) or L40S 48GB (fp8)
- Currently served on OpenRouter only by SiliconFlow (China-based), so no
  compliant EU option exists today
- Reasoning models are where EU enterprise pain is sharpest right now

Secondary candidate: `bytedance/ui-tars-1.5-7b` — 7B UI agent model, trivially
cheap to serve, adds a second SKU once the stack is stable.

## Roadmap

### Phase 1 — Validate the gap
- [ ] Latency-test QwQ via OpenRouter from a Frankfurt VM (confirm non-EU origin)
- [ ] Confirm SiliconFlow has no EU endpoint
- [ ] Contact OpenRouter enterprise to ask which open-weight models lack EU coverage

### Phase 2 — Bring one endpoint live
- [ ] Provision 1×H100 in Frankfurt (Lambda / Crusoe / Hetzner GPU)
- [ ] vLLM or SGLang serving config for QwQ-32B
- [ ] OpenAI-compatible API with streaming, tool calls, structured outputs
- [ ] Uptime and latency benchmarks vs SiliconFlow from EU callers
- [ ] No-logging / no-training privacy posture, documented

### Phase 3 — Apply to OpenRouter
- [ ] German legal entity (UG or GmbH) and DPA template
- [ ] Draft OpenRouter provider application with QwQ as the headline launch model
- [ ] Submit and iterate

### Phase 4 — Expand
- [ ] Add `ui-tars-1.5-7b` as a second SKU
- [ ] Evaluate adding a 70B-class model (Hermes 4 70B, Qwen2.5-VL-72B) once the
      single-GPU stack is stable
- [ ] Direct EU enterprise sales off OpenRouter (LinkedIn, compliance content)

## Status

Pre-launch. Public build log on
[Substack](https://maxhager28.substack.com).

## Team

Max Hager · Max Schleper
