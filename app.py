<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Resume Ranker</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #0b0d17; }
        .glass-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); }
        .gradient-text { background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .btn-gradient { background: linear-gradient(90deg, #3b82f6, #a855f7); }
    </style>
</head>
<body class="text-white p-8 font-sans">

    <div class="max-w-6xl mx-auto flex gap-6">
        
        <!-- Sidebar -->
        <aside class="w-1/4 space-y-6">
            <div class="glass-card p-6 rounded-2xl">
                <div class="bg-blue-600 w-10 h-10 rounded-lg flex items-center justify-center mb-4">
                    <i class="fas fa-file-alt"></i>
                </div>
                <h1 class="text-2xl font-bold">AI Resume <br><span class="text-blue-400">Ranker</span></h1>
                <p class="text-gray-400 text-sm mt-4 leading-relaxed">
                    Upload resumes and get AI-powered ranking based on job description matching.
                </p>
            </div>

            <div class="space-y-4">
                <div class="flex gap-4">
                    <div class="text-purple-400"><i class="fas fa-bolt"></i></div>
                    <div>
                        <h4 class="text-sm font-semibold">Smart Matching</h4>
                        <p class="text-xs text-gray-500">TF-IDF & Cosine Similarity</p>
                    </div>
                </div>
                <div class="flex gap-4">
                    <div class="text-green-400"><i class="fas fa-shield-alt"></i></div>
                    <div>
                        <h4 class="text-sm font-semibold">Privacy First</h4>
                        <p class="text-xs text-gray-500">Securely processed</p>
                    </div>
                </div>
            </div>

            <div class="glass-card p-4 rounded-xl mt-10">
                <p class="text-xs text-blue-300 italic">⭐ Tip: Be specific in the job description to get better results.</p>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="w-3/4 glass-card rounded-2xl p-8 relative">
            <div class="absolute top-6 right-6">
                <button class="text-xs border border-gray-600 px-3 py-1 rounded-full flex items-center gap-2 hover:bg-gray-800 transition">
                    <i class="fas fa-sun text-yellow-400"></i> Light Mode
                </button>
            </div>

            <div class="text-center mb-10">
                <h2 class="text-4xl font-bold mb-2">AI <span class="gradient-text underline decoration-purple-500">Resume Ranker</span></h2>
                <p class="text-gray-400 text-sm">Find the best candidates for your job role using AI</p>
            </div>

            <!-- Job Description Input -->
            <div class="mb-8">
                <div class="flex items-center gap-3 mb-3">
                    <div class="bg-purple-900/30 p-2 rounded-lg text-purple-400"><i class="fas fa-briefcase"></i></div>
                    <label class="font-medium">Enter Job Description</label>
                </div>
                <textarea 
                    class="w-full h-32 bg-black/40 border border-gray-700 rounded-xl p-4 text-sm focus:outline-none focus:border-purple-500 transition"
                    placeholder="e.g. We are looking for a Data Scientist..."></textarea>
                <p class="text-right text-[10px] text-gray-500 mt-1">0 / 5000</p>
            </div>

            <!-- Upload Section -->
            <div class="mb-8">
                <div class="flex items-center gap-3 mb-3">
                    <div class="bg-green-900/30 p-2 rounded-lg text-green-400"><i class="fas fa-upload"></i></div>
                    <label class="font-medium">Upload Resumes (PDF)</label>
                </div>
                <div class="border-2 border-dashed border-gray-700 rounded-xl p-10 text-center flex flex-col items-center hover:border-blue-500 transition cursor-pointer">
                    <i class="fas fa-cloud-upload-alt text-4xl text-blue-400 mb-4"></i>
                    <p class="text-sm font-semibold">Drag & Drop PDF files here</p>
                    <p class="text-xs text-gray-500 my-2">or</p>
                    <button class="btn-gradient px-6 py-2 rounded-lg text-sm font-bold shadow-lg">Browse Files</button>
                    <p class="text-[10px] text-gray-500 mt-4"><i class="fas fa-file-pdf mr-1"></i> Max 200MB per file</p>
                </div>
            </div>

            <!-- Action Button -->
            <button class="w-full btn-gradient py-4 rounded-xl font-bold flex items-center justify-center gap-3 text-lg hover:opacity-90 transition shadow-2xl">
                <i class="fas fa-trophy"></i> Rank Resumes
            </button>

            <!-- Bottom Stats -->
            <div class="grid grid-cols-3 gap-6 mt-12 pt-8 border-t border-gray-800">
                <div class="flex items-center gap-3">
                    <i class="fas fa-users text-blue-400 text-xl"></i>
                    <div><p class="text-xs font-bold">AI Powered</p><p class="text-[10px] text-gray-500">Smart candidate matching</p></div>
                </div>
                <div class="flex items-center gap-3">
                    <i class="fas fa-bullseye text-blue-400 text-xl"></i>
                    <div><p class="text-xs font-bold">Accurate Ranking</p><p class="text-[10px] text-gray-500">Based on content similarity</p></div>
                </div>
                <div class="flex items-center gap-3">
                    <i class="fas fa-lock text-blue-400 text-xl"></i>
                    <div><p class="text-xs font-bold">100% Secure</p><p class="text-[10px] text-gray-500">Your data is safe with us</p></div>
                </div>
            </div>
        </main>
    </div>

</body>
</html>