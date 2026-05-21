# [002] Use Python

## Status - ACTIVE

## Context

**MadChatter** should be a web based application that requires a backend framework. Since there will
be heavy AI integration, as well as the need for a stable web server, we identified the following
requirements for a choice of backend language:
- Easy integration of AI models
  - Includes TTS, STT, LLMs, RAG.
- Ecosystem for developing web servers.

## Decided Approach

We will implement the backend using [Python](https://www.python.org/). Some reeasons include:
- Strong AI ecosystem.
- Strong support for AI frameworks and tooling (STT, TTS, LLMs, RAG).
- Fast prototyping possibilities
- Existing web frameworks

## Consequences

Pros:
- Fast development speeds.
- Reduced workload for integrating AI features.
Cons:
- Python is not the fastest language, and may be inferior in terms of speed when compared to other languages.
- No static typing.