# ─── SCHOLARSHIP KNOWLEDGE BASE ─────────────────────────────────────────────
# This is the data your RAG system will search through.
# Add/edit any rules here — they get embedded into ChromaDB automatically.

SCHOLARSHIP_DOCS = [

    # ── ELIGIBILITY ──────────────────────────────────────────────────────────
    {
        "id": "elig_001",
        "text": """
        Merit Excellence Award eligibility:
        - Minimum academic marks: 85% or above
        - Family annual income: No income limit
        - Coverage: Full tuition fee + monthly stipend of Rs 2000
        - Course: Any undergraduate or postgraduate program
        - Documents needed: Mark sheet, ID proof, admission letter
        """,
        "metadata": {"category": "eligibility", "scholarship": "merit_excellence"}
    },
    {
        "id": "elig_002",
        "text": """
        Need-Based Financial Aid eligibility:
        - Minimum academic marks: 50% or above
        - Family annual income: Must be below Rs 2,00,000 per year
        - Coverage: Up to Rs 50,000 per year for tuition and books
        - Course: Any recognized degree program
        - Documents needed: Income certificate, mark sheet, ID proof, bank details
        """,
        "metadata": {"category": "eligibility", "scholarship": "need_based"}
    },
    {
        "id": "elig_003",
        "text": """
        Merit-cum-Means Scholarship eligibility:
        - Minimum academic marks: 75% or above
        - Family annual income: Must be Rs 3,00,000 or below per year
        - Coverage: Up to Rs 30,000 per year
        - Course: Any recognized undergraduate program
        - Documents needed: Mark sheet, income certificate, ID proof, admission letter
        This is the most common and popular scholarship on ScholarPath.
        """,
        "metadata": {"category": "eligibility", "scholarship": "merit_cum_means"}
    },
    {
        "id": "elig_004",
        "text": """
        Sports Achievement Scholarship eligibility:
        - Minimum academic marks: 50% or above
        - Must have represented state or national level in any sport
        - Family annual income: Must be below Rs 5,00,000 per year
        - Coverage: Up to Rs 25,000 per year
        - Documents needed: Sports certificate, mark sheet, income certificate, ID proof
        """,
        "metadata": {"category": "eligibility", "scholarship": "sports"}
    },

    # ── GENERAL ELIGIBILITY RULES ─────────────────────────────────────────────
    {
        "id": "elig_005",
        "text": """
        General eligibility rules for all scholarships on ScholarPath:
        - Student must be an Indian citizen
        - Must be enrolled in a recognized institution
        - Cannot hold more than one scholarship at a time
        - Age limit: 17 to 30 years for undergraduate, up to 35 for postgraduate
        - Minimum marks of 75% and income below Rs 3,00,000 qualifies as ELIGIBLE
        - Marks between 60-75% and income below Rs 5,00,000 is CONDITIONALLY ELIGIBLE
        - Below these thresholds is marked as NOT ELIGIBLE
        """,
        "metadata": {"category": "eligibility", "scholarship": "all"}
    },

    # ── DOCUMENTS ─────────────────────────────────────────────────────────────
    {
        "id": "docs_001",
        "text": """
        Required documents for scholarship application:
        1. Mark Sheet or Transcript - shows your academic percentage
        2. Income Certificate - issued by government authority showing annual family income
        3. Government ID Proof - Aadhaar card, PAN card, or Passport
        4. Admission Letter - from your college or university
        5. Bank Account Details - cancelled cheque or passbook copy for disbursement
        All documents must be uploaded as PNG, JPG, or PDF files.
        Maximum file size is 16MB per document.
        """,
        "metadata": {"category": "documents"}
    },
    {
        "id": "docs_002",
        "text": """
        How OCR document verification works on ScholarPath:
        - After you upload a document, our system uses OpenCV to preprocess the image
        - The image is converted to grayscale and binarized to improve clarity
        - Tesseract OCR then extracts text from the processed image
        - The system uses regex patterns to find your marks percentage and income amount
        - These extracted values are compared with what you declared in the form
        - If OCR finds different values, the system updates your eligibility automatically
        - Admin can view the raw OCR text during their review
        """,
        "metadata": {"category": "documents", "topic": "ocr"}
    },

    # ── APPLICATION PROCESS ───────────────────────────────────────────────────
    {
        "id": "proc_001",
        "text": """
        How to apply for a scholarship on ScholarPath - step by step:
        Step 1: Register on ScholarPath with your email and create a password
        Step 2: Login to your student dashboard
        Step 3: Click 'Apply Now' and fill in your scholarship application form
        Step 4: Enter your academic marks and family income accurately
        Step 5: Upload your supporting documents (mark sheet, income certificate, ID)
        Step 6: Wait for OCR processing - this happens automatically within minutes
        Step 7: Admin reviews your application and OCR extracted data
        Step 8: You receive approval or rejection notification on your dashboard
        Step 9: If approved, scholarship amount is processed and disbursed to your bank
        """,
        "metadata": {"category": "process"}
    },
    {
        "id": "proc_002",
        "text": """
        Application status meanings on ScholarPath:
        - PENDING: Your application has been submitted and is waiting for admin review
        - APPROVED: Admin has approved your application, scholarship will be disbursed
        - REJECTED: Application was not approved, check admin remarks for reason
        - PROCESSING: Payment is being processed to your bank account
        - DISBURSED: Scholarship amount has been sent to your bank account
        Auto eligibility status:
        - ELIGIBLE: You meet all criteria (75%+ marks, income below Rs 3 lakh)
        - CONDITIONALLY ELIGIBLE: Partial criteria met, needs manual admin review
        - NOT ELIGIBLE: Does not meet minimum criteria
        - MANUAL REVIEW: OCR could not extract data, admin will verify manually
        """,
        "metadata": {"category": "process", "topic": "status"}
    },

    # ── FAQ ───────────────────────────────────────────────────────────────────
    {
        "id": "faq_001",
        "text": """
        Frequently asked questions about ScholarPath:
        Q: Can I apply for multiple scholarships?
        A: No, you can only hold one scholarship at a time on ScholarPath.

        Q: How long does approval take?
        A: Admin reviews typically take 3 to 7 working days after document upload.

        Q: What if my OCR data is wrong?
        A: Admin reviews the raw OCR output manually. You can also re-upload a clearer image.

        Q: When will I receive the money?
        A: After admin approves, disbursement takes 5 to 10 working days to your bank.

        Q: Can I edit my application after submitting?
        A: You can upload additional documents but cannot edit the form once submitted.

        Q: What if my income certificate is in Hindi or another language?
        A: English documents give the best OCR results. For other languages, admin will verify manually.
        """,
        "metadata": {"category": "faq"}
    },
    {
        "id": "faq_002",
        "text": """
        More frequently asked questions:
        Q: I scored 74% marks. Am I eligible?
        A: You just miss the Merit-cum-Means threshold of 75%. You may qualify as Conditionally Eligible 
           if your income is below Rs 5 lakh. Admin will review your case.

        Q: My family income is Rs 3,50,000. Which scholarship can I apply for?
        A: You do not qualify for Merit-cum-Means (limit Rs 3 lakh) but may qualify for 
           Need-Based Aid if your marks are 50%+ and income is below Rs 5 lakh conditionally.

        Q: Do I need to renew the scholarship every year?
        A: Yes, you must submit a fresh application each academic year with updated documents.

        Q: Is there an application fee?
        A: No. ScholarPath is completely free to use for students.
        """,
        "metadata": {"category": "faq"}
    },

    # ── CONTACT & SUPPORT ─────────────────────────────────────────────────────
    {
        "id": "support_001",
        "text": """
        ScholarPath support and contact information:
        - For technical issues with document upload, try a clearer image or PDF format
        - For eligibility queries, check the eligibility criteria section on the home page
        - Admin contact is available through the application remarks section
        - Processing time: Document OCR is instant, admin review takes 3-7 working days
        - Office hours: Admin panel is reviewed Monday to Friday, 9am to 5pm
        """,
        "metadata": {"category": "support"}
    },
]