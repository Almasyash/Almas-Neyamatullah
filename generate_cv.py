import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_cv():
    pdf_path = "Almas_Neyamatullah_CV.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    PRIMARY = colors.HexColor("#cc2222")    # Crimson Accent
    DARK = colors.HexColor("#141416")       # Dark Charcoal
    TEXT = colors.HexColor("#2d2d30")       # Body Text
    MUTED = colors.HexColor("#555558")      # Subtitle / Muted Text
    LINE = colors.HexColor("#dcdcd8")       # Divider line
    ACCENT_BG = colors.HexColor("#f8f8f9")  # Subtle skill box background

    styles = getSampleStyleSheet()

    # Custom typography styles
    style_name = ParagraphStyle(
        'CVName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=21,
        leading=25,
        alignment=TA_CENTER,
        textColor=DARK
    )

    style_title = ParagraphStyle(
        'CVTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=PRIMARY
    )

    style_contact = ParagraphStyle(
        'CVContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        alignment=TA_CENTER,
        textColor=MUTED
    )

    style_section = ParagraphStyle(
        'CVSection',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=DARK,
        spaceBefore=8,
        spaceAfter=2
    )

    style_item_title = ParagraphStyle(
        'CVItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=DARK
    )

    style_item_subtitle = ParagraphStyle(
        'CVItemSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=PRIMARY
    )

    style_date = ParagraphStyle(
        'CVDate',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        alignment=TA_RIGHT,
        textColor=MUTED
    )

    style_body = ParagraphStyle(
        'CVBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.2,
        textColor=TEXT,
        alignment=TA_JUSTIFY
    )

    style_bullet = ParagraphStyle(
        'CVBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT,
        leftIndent=12,
        firstLineIndent=-10
    )

    style_skill_label = ParagraphStyle(
        'CVSkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=DARK
    )

    style_skill_val = ParagraphStyle(
        'CVSkillVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT
    )

    elements = []

    # 1. HEADER SECTION
    elements.append(Paragraph("ALMAS NEYAMATULLAH", style_name))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("Founder, MAHMAS GROUP &middot; Full Stack Developer &middot; Mobile App Engineer &middot; UI/UX Specialist", style_title))
    elements.append(Spacer(1, 3))
    
    contact_text = (
        "Bettiah, West Champaran, Bihar, India &nbsp;|&nbsp; "
        "Phone: <b>+91 7033761519</b> &nbsp;|&nbsp; "
        "Email: <b>almasneyamt786@gmail.com</b><br/>"
        "Portfolio: <b>almasyash.github.io/Almas-Neyamatullah/</b> &nbsp;|&nbsp; "
        "GitHub: <b>github.com/Almasyash</b> &nbsp;|&nbsp; "
        "LinkedIn: <b>linkedin.com/in/almas-neyamatullah</b>"
    )
    elements.append(Paragraph(contact_text, style_contact))
    elements.append(Spacer(1, 5))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=2, spaceAfter=6))

    # 2. PROFESSIONAL SUMMARY
    elements.append(Paragraph("PROFESSIONAL SUMMARY", style_section))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=1, spaceAfter=4))
    summary_text = (
        "Versatile <b>Full Stack Software Developer</b> and <b>Mobile Application Engineer</b> with a proven track record "
        "of building high-performance web applications, native Android software, and custom business platforms. "
        "Founder of <b>MAHMAS GROUP</b>, an official Government of India MSME-registered enterprise (UDYAM-BR-38-0075911) based in Bettiah, Bihar. "
        "Passionate about delivering cutting-edge digital experiences, scalable cloud backends, seamless WhatsApp commerce integrations, "
        "and clean user-centric UI/UX architectures."
    )
    elements.append(Paragraph(summary_text, style_body))
    elements.append(Spacer(1, 6))

    # 3. WORK EXPERIENCE & ENTREPRENEURSHIP
    elements.append(Paragraph("EXPERIENCE &amp; ENTREPRENEURSHIP", style_section))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=1, spaceAfter=4))

    # Job 1: MAHMAS GROUP
    row1 = [
        Paragraph("<b>Founder &amp; Lead Developer</b> &middot; MAHMAS GROUP", style_item_title),
        Paragraph("Bettiah, Bihar | 2023 – Present", style_date)
    ]
    t1 = Table([row1], colWidths=[380, 160])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(t1)
    elements.append(Paragraph("<i>Government Registered Micro Enterprise (UDYAM-BR-38-0075911 &middot; NIC 6201 Web &amp; Software Development)</i>", style_item_subtitle))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("&bull; Architected and deployed modern showcase and e-commerce websites for regional businesses, clinics, and institutions with custom 1-tap WhatsApp order pipelines.", style_bullet))
    elements.append(Paragraph("&bull; Engineered offline-first local billing and inventory software tailored for shop counters, providing receipt printing, sales reports, and customer khata management.", style_bullet))
    elements.append(Paragraph("&bull; Successfully verified, ranked, and optimized Google Business Profile listings for local enterprises, driving high local search visibility.", style_bullet))
    elements.append(Paragraph("&bull; Directed client technology workflows at <i>MAHMAS Digital Cafe</i> and authored programming video tutorials on YouTube channel <i>Code With MAHMAS</i>.", style_bullet))
    elements.append(Spacer(1, 5))

    # Job 2: Freelance Full-Stack Developer
    row2 = [
        Paragraph("<b>Full-Stack Web &amp; Mobile Developer</b> &middot; Freelance", style_item_title),
        Paragraph("Remote / India | 2021 – Present", style_date)
    ]
    t2 = Table([row2], colWidths=[380, 160])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(t2)
    elements.append(Paragraph("&bull; Designed responsive user interfaces in Figma and developed end-to-end full stack web platforms using React, Node.js, Express, and REST APIs.", style_bullet))
    elements.append(Paragraph("&bull; Built and released native Android utilities (APKs) with smooth media playback and custom UI components.", style_bullet))
    elements.append(Paragraph("&bull; Designed intuitive UI/UX prototypes and wireframes in Figma, translating concepts into pixel-perfect responsive web components.", style_bullet))
    elements.append(Spacer(1, 6))

    # 4. KEY FEATURED PROJECTS
    elements.append(Paragraph("KEY FEATURED PROJECTS", style_section))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=1, spaceAfter=4))

    # Project 1: Pet's Heaven
    p1 = [
        Paragraph("<b>Pet's Heaven &middot; Web Platform &amp; Android App</b>", style_item_title),
        Paragraph("<b>Live Platform &middot; petsheaven.in</b>", style_date)
    ]
    tp1 = Table([p1], colWidths=[360, 180])
    tp1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    elements.append(tp1)
    elements.append(Paragraph("&bull; <b>Tech:</b> HTML5, CSS3, JavaScript, Android SDK, Responsive UI/UX Architecture", style_bullet))
    elements.append(Paragraph("&bull; Built an end-to-end pet-care portal providing service booking, veterinary showcases, and a companion native Android APK.", style_bullet))
    elements.append(Spacer(1, 4))

    # Project 2: E-Commerce Platform
    p2 = [
        Paragraph("<b>Full-Stack E-Commerce Website &amp; Admin Suite</b>", style_item_title),
        Paragraph("<b>almasyash.github.io/E-COMMERCE-WEBSITE</b>", style_date)
    ]
    tp2 = Table([p2], colWidths=[330, 210])
    tp2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    elements.append(tp2)
    elements.append(Paragraph("&bull; <b>Tech:</b> React.js, TypeScript, Node.js, Express.js, RESTful APIs, LocalStorage/Database", style_bullet))
    elements.append(Paragraph("&bull; Developed high-conversion customer storefront with cart state management, checkout workflow, and administrative catalog controls.", style_bullet))
    elements.append(Spacer(1, 4))

    # Project 3: Editor FS
    p3 = [
        Paragraph("<b>Editor FS &middot; Android Video Editing Application</b>", style_item_title),
        Paragraph("<b>github.com/FS-Groupz/Editor-FS</b>", style_date)
    ]
    tp3 = Table([p3], colWidths=[350, 190])
    tp3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    elements.append(tp3)
    elements.append(Paragraph("&bull; <b>Tech:</b> Android SDK, Java/Kotlin, Media Pipeline, APK Release &amp; Optimization", style_bullet))
    elements.append(Paragraph("&bull; Implemented an interactive timeline editor with real-time video playback, audio mixing filters, and rapid export pipeline.", style_bullet))
    elements.append(Spacer(1, 4))

    # Project 4: To-Do List App
    p4 = [
        Paragraph("<b>To-Do List &middot; Interactive Task Manager &amp; Workflow Tool</b>", style_item_title),
        Paragraph("<b>almasyash.github.io/Almas-Neyamatullah</b>", style_date)
    ]
    tp4 = Table([p4], colWidths=[360, 180])
    tp4.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    elements.append(tp4)
    elements.append(Paragraph("&bull; <b>Tech:</b> JavaScript (ES6+), LocalStorage, HTML5, CSS3 Glassmorphism, CRUD Engine", style_bullet))
    elements.append(Paragraph("&bull; Built a fast, responsive personal productivity web application with persistent offline storage, task categorization, and smart priority filters.", style_bullet))
    elements.append(Spacer(1, 6))

    # 5. CORE SKILLS & EXPERTISE
    elements.append(Paragraph("TECHNICAL &amp; DESIGN EXPERTISE", style_section))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=1, spaceAfter=4))

    skills_data = [
        [Paragraph("<b>Web &amp; Frontend:</b>", style_skill_label), Paragraph("JavaScript (ES6+), React.js, TypeScript, HTML5, CSS3, Responsive Design, State Management", style_skill_val)],
        [Paragraph("<b>Backend &amp; APIs:</b>", style_skill_label), Paragraph("Node.js, Express.js, Python, REST APIs, JSON Architecture, LocalStorage, Database Design", style_skill_val)],
        [Paragraph("<b>Mobile Development:</b>", style_skill_label), Paragraph("Android Development, APK Architecture, Java, Kotlin, Flutter / Dart basics", style_skill_val)],
        [Paragraph("<b>UI/UX &amp; Design:</b>", style_skill_label), Paragraph("UI/UX Design, Figma, Wireframing, Responsive Layouts, User Flow, Adobe Photoshop, Illustrator, Visual Design", style_skill_val)],
        [Paragraph("<b>Tools &amp; Workflow:</b>", style_skill_label), Paragraph("Git, GitHub, VS Code, Playwright Automation, Linux, Windows, Localhost Dev Servers", style_skill_val)]
    ]
    t_skills = Table(skills_data, colWidths=[120, 420])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    elements.append(t_skills)
    elements.append(Spacer(1, 6))

    # 6. GOVERNMENT MSME CREDENTIALS
    elements.append(Paragraph("OFFICIAL CREDENTIALS &amp; CERTIFICATION", style_section))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=1, spaceAfter=4))

    cert_data = [
        [
            Paragraph("<b>Enterprise Name:</b> MAHMAS (MAHMAS GROUP)", style_body),
            Paragraph("<b>Udyam Reg. No.:</b> <font color='#cc2222'><b>UDYAM-BR-38-0075911</b></font>", style_body)
        ],
        [
            Paragraph("<b>Ministry:</b> Ministry of MSME, Govt. of India", style_body),
            Paragraph("<b>Classification:</b> Micro Enterprise &middot; Services (NIC 6201)", style_body)
        ]
    ]
    t_cert = Table(cert_data, colWidths=[270, 270])
    t_cert.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    elements.append(t_cert)

    doc.build(elements)
    print("SUCCESS: Almas_Neyamatullah_CV.pdf built successfully!")

if __name__ == "__main__":
    build_cv()
