e# 🔤 Natural Language Processing (CS-442)

Welcome to the **Natural Language Processing (NLP)** course repository! This directory houses lecture presentations, course outlines, mathematical blueprints, and state-of-the-art transformer paper study decks completed during Semester 8.

Delivered by **Dr. Muzamil Ahmed**, this course covers the journey of computational linguistics from traditional statistical language models to modern Deep Learning representations and Pre-trained Transformer Architectures.

---

## 📂 Directory Contents

This directory contains the following academic and technical resources:

*   **📘 Course Roadmap & Outlines**:
    *   [NLP Course Outline.pdf](./NLP%20Course%20Outline.pdf) — Course syllabus, learning outcomes, grading breakdown, and reference literature.
*   **📐 Mathematical Foundation & Architecture Blueprints**:
    *   [NLP_Mathematical_Blueprint.pdf](./NLP_Mathematical_Blueprint.pdf) — Detailed mathematical derivations for vector spaces, loss functions, tokenization, and neural language model backpropagation.
    *   [Neural_Embedding_Architectures.pdf](./Neural_Embedding_Architectures.pdf) — Comprehensive guide on continuous vector representations, Word2Vec (CBOW & Skip-gram), and GloVe embedding spaces.
*   **📑 Lecture Slide Series (Lectures 01 to 11)**:
    *   [LEC 1 NLP by Dr. Muzamil Ahmed.pptx](./LEC%201%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Introduction to Natural Language Processing, text preprocessing, and tokenization.
    *   [LEC 2 NLP by Dr. Muzamil Ahmed.pptx](./LEC%202%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — N-gram Language Modeling, Smoothing algorithms (Add-1, Good-Turing, Kneser-Ney).
    *   [LEC 3 NLP by Dr. Muzamil Ahmed.pptx](./LEC%203%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Text Classification, Naive Bayes, and Sentiment Analysis.
    *   [LEC 4  NLP by Dr. Muzamil Ahmed.pptx](./LEC%204%20%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Vector Semantics, TF-IDF, Cosine Similarity, and Latent Semantic Analysis (LSA).
    *   [LEC 5  NLP by Dr. Muzamil Ahmed.pptx](./LEC%205%20%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Word Embeddings: Word2Vec (Skip-Gram & Continuous Bag-of-Words) and GloVe.
    *   [LEC 6 NLP RNN + LSTM by Dr. Muzamil Ahmed.pptx](./LEC%206%20NLP%20RNN%20%2B%20LSTM%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Recurrent Architectures: Vanilla RNNs, vanishing gradients, LSTM cell gates, and GRU units.
    *   [LEC 7 NLP by Dr. Muzamil Ahmed.pptx](./LEC%207%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Encoder-Decoder Seq2Seq models, Machine Translation, and Attention Mechanisms.
    *   [LEC 8 NLP by Dr. Muzamil Ahmed.pptx](./LEC%208%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Transformer Architecture: Self-Attention, Multi-Head Attention, and Positional Encodings.
    *   [LEC 9 NLP by Dr. Muzamil Ahmed.pptx](./LEC%209%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Pre-trained Language Models & Transfer Learning in NLP.
    *   [LEC 10 NLP by Dr. Muzamil Ahmed.pptx](./LEC%2010%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Masked Language Modeling (MLM), Fine-Tuning strategies, and Downstream Task adaptation.
    *   [LEC 11 NLP by Dr. Muzamil Ahmed.pptx](./LEC%2011%20NLP%20by%20Dr.%20Muzamil%20Ahmed.pptx) — Advanced Generative Architectures, Prompting strategies, and Large Language Model (LLM) paradigms.
*   **🚀 Advanced Transformer Models & Landmark Research**:
    *   [BERT.pdf](./BERT.pdf) — *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* (Devlin et al.).
    *   [ELMo.pptx](./ELMo.pptx) — *Deep Contextualized Word Representations (Embeddings from Language Models)*.
    *   [Roberta.pptx](./Roberta.pptx) — *RoBERTa: A Robustly Optimized BERT Pretraining Approach* (Liu et al.).
    *   [XLNet.pptx](./XLNet.pptx) — *XLNet: Generalized Autoregressive Pretraining for Language Understanding*.
*   **🔗 Official Code & Semester Project Repository**:
    *   🔗 **[Robust Sentiment and Emotion Classification on Noisy Urdu Tweets](https://github.com/abubakarp789/Robust-Sentiment-and-Emotion-Classification-on-Noisy-Urdu-Tweets)** — Code repository housing 4 course assignments (`Assignment#01` to `Assignment#04`) and the final semester research project on noisy Urdu tweet classification.

---

## 🛠️ Architecture Evolution Pipeline

```text
  ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
  │  TF-IDF & N-gram │ ───► │ Word Embeddings  │ ───► │  Seq2Seq / LSTM  │
  │ (Bag of Words)   │      │(Word2Vec/GloVe)  │      │(Recurrent Gates) │
  └──────────────────┘      └──────────────────┘      └─────────┬────────┘
                                                                │
                                                                ▼
  ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
  │ RoBERTa / XLNet  │ ◄─── │     B E R T      │ ◄─── │ Self-Attention   │
  │ (Optimized LLMs) │      │(Bidirectional LM)│      │  (Transformers)  │
  └──────────────────┘      └──────────────────┘      └──────────────────┘
```

---

## 🧠 Core Competencies & Key Concepts

### 1. Vector Semantics & Word Embeddings
*   **Static vs. Dynamic Embeddings**: Shift from static frequency vectors (TF-IDF) to continuous contextual representations (ELMo, Word2Vec).
*   **Vector Geometry**: Cosine distance operations capturing semantic relations (e.g., `King - Man + Woman = Queen`).

### 2. Recurrent & Sequential Modeling
*   **LSTM & GRU Dynamics**: Addressing vanishing and exploding gradients over long sequence windows via forget, input, and output gates.
*   **Seq2Seq & Attention**: Translating sequences using Context Vectors enhanced by Bahdanau and Luong Attention mechanisms.

### 3. Modern Transformer Paradigms
*   **Self-Attention Mathematics**: Computing Query ($Q$), Key ($K$), and Value ($V$) matrices ($Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$).
*   **Encoder-Decoder Frameworks**: Masked Language Modeling (BERT), Permutation Language Modeling (XLNet), and Dynamic Masking optimization (RoBERTa).

---

*Navigate through the presentations and PDFs above for detailed mathematical derivations and research papers!*
