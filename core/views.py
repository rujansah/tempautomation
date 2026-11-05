from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["services"] = [
            {"icon": "💻", "title": "Tech Solutions", "desc": "End-to-end IT Support, automation & VAPT."},
            {"icon": "📚", "title": "Courses & Training", "desc": "Hands-on programs in DevOps, Cloud, Security & Python."},
            {"icon": "🧑‍💻", "title": "Individual Support", "desc": "One-on-one troubleshooting and mentorship."},
            {"icon": "🤝", "title": "Community & Collab", "desc": "Contribute, network, and build with experts."},
        ]

        ctx["supports"] = [
            {"t": "Windows & Automation", "d": "PowerShell, Python, agents & dashboards."},
            {"t": "Cloud & DevOps", "d": "CI/CD, Docker, Kubernetes, monitoring."},
            {"t": "Security & VAPT", "d": "Assessments, hardening, best practices."},
        ]
        return ctx

class CoursesView(TemplateView):
    template_name = 'core/courses.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["courses"] = [
            {
                "title": "Python for Automation",
                "duration": "6 Weeks",
                "desc": "Master Python for scripting and automation of tasks.",
            },
            {
                "title": "DevOps Bootcamp",
                "duration": "8 Weeks",
                "desc": "CI/CD pipelines, Docker, Kubernetes, and real projects.",
            },
            {
                "title": "Cloud Essentials (AWS/Azure)",
                "duration": "6 Weeks",
                "desc": "Learn cloud deployment and scaling on AWS & Azure.",
            },
            {
                "title": "Web Security (VAPT)",
                "duration": "4 Weeks",
                "desc": "Learn penetration testing, OWASP, and secure coding.",
            },
            {
                "title": "Full-Stack Development",
                "duration": "10 Weeks",
                "desc": "React, Django, APIs, and databases with projects.",
            },
            {
                "title": "AI & Data Science",
                "duration": "12 Weeks",
                "desc": "Machine learning, data analysis, and visualization.",
            },
            {
                "title": "CCNA (Cisco Certified Network Associate)",
                "duration": "8 Weeks",
                "desc": "Networking fundamentals, routing, switching, and network security basics.",
            },
            {
                "title": "CCNP (Cisco Certified Network Professional)",
                "duration": "10 Weeks",
                "desc": "Advanced routing, switching, troubleshooting, and enterprise networking.",
            },
            {
                "title": "CCIE (Cisco Certified Internetwork Expert)",
                "duration": "16 Weeks",
                "desc": "Expert-level networking with real-world lab scenarios and deep technical mastery.",
            },
            {
                "title": "MCSE (Microsoft Certified Solutions Expert)",
                "duration": "10 Weeks",
                "desc": "Windows Server, Active Directory, networking, and enterprise infrastructure.",
            },
            {
                "title": "CEH (Certified Ethical Hacker)",
                "duration": "6 Weeks",
                "desc": "Ethical hacking, penetration testing tools, and vulnerability assessment.",
            },
            {
                "title": "OSCP (Offensive Security Certified Professional)",
                "duration": "12 Weeks",
                "desc": "Hands-on penetration testing, exploit development, and real-world hacking labs.",
            },
            {
                "title": "CompTIA A+",
                "duration": "6 Weeks",
                "desc": "IT fundamentals, hardware, software troubleshooting, and support skills.",
            },
            {
                "title": "CompTIA Network+",
                "duration": "6 Weeks",
                "desc": "Networking concepts, infrastructure, operations, and security basics.",
            },
            {
                "title": "CompTIA Security+",
                "duration": "6 Weeks",
                "desc": "Cybersecurity fundamentals, risk management, and network security.",
            },
        ]
        return ctx

class ServicesView(TemplateView):
    template_name = 'core/services.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["services"] = [
            {
                "icon": "🖥️",
                "title": "Server Solutions",
                "desc": "Deployment, management, and optimization of enterprise servers.",
                "image": "serverimage.jpg"

            },
            {
                "icon": "🌐",
                "title": "Network Solutions",
                "desc": "Reliable and secure networking for scalable business operations.",
                "image": "networksolutionimage.jpg"
            },
            {
                "icon": "⚙️",
                "title": "Automation & Systems",
                "desc": "Automating workflows and infrastructure for efficiency.",
                "image": "automationsystemimage.jpg"
            },
            {
                "icon": "🔒",
                "title": "Security & VAPT",
                "desc": "Enterprise-grade protection with vulnerability assessment and penetration testing.",
                "image": "vaptimage2.png"
            },
            {
                "icon": "☁️",
                "title": "Cloud Solutions",
                "desc": "Cloud migration, optimization, and hybrid infrastructure support.",
                "image": "cloudsolutionimage.jpg"
            },
            {
                "icon": "🏢",
                "title": "Enterprise Support",
                "desc": "End-to-end system support tailored for enterprise environments.",
                "image": "enterprisesupportimage.jpg"
            },
            {
                "icon": "📹",
                "title": "CCTV Surveillance",
                "desc": "24/7 CCTV surveillance service (365 days) at $250/month for complete security monitoring.",
                "image": "cctvimage.jpg"
            },
        ]
        return ctx



class AboutView(TemplateView):
    template_name = 'core/about.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["team"] = [
            {"name": "Rujjj", "role": "Founder & Tech Lead"},
            {"name": "Priya", "role": "Cybersecurity Analyst"},
            {"name": "Arjun", "role": "DevOps Engineer"},
            {"name": "Sneha", "role": "Course Instructor"},
        ]
        return ctx

class ContactView(TemplateView):
    template_name = 'core/contact.html'
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"This mail is from Contact Page of kgtech.com.np \n\n From: {name} <{email}>\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,   # from email
            settings.CONTACT_RECIPIENT_EMAILS          # recipient email
        )
        return redirect("contact")

class SupportView(TemplateView):
    template_name = 'core/support.html'

class PrivacyView(TemplateView):
    template_name = 'core/privacy.html'

class TermsView(TemplateView):
    template_name = 'core/terms.html'



class ProductsView(TemplateView):
    template_name = "core/products.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        products = [
            # Your FULL 72 product list here

            {"model": "RG-ES05F", "description": "5-Port 10/100 Mbps Desktop Plastic Switch", "si_price": "1,040.00", "msrp": "1,240.00", "warranty": "3 Years", "image": "RG-ES05F.jpeg"},
            {"model": "RG-ES05G-L", "description": "5-Port Gigabit unmanaged Switch, 5 Gigabit RJ45 Ports, Plastic Case", "si_price": "1,770.00", "msrp": "2,120.00", "warranty": "3 Years", "image": "RG-ES05G-L.jpeg"},
            {"model": "RG-ES08F", "description": "8-Port 10/100 Mbps Desktop Plastic Switch", "si_price": "1,230.00", "msrp": "1,470.00", "warranty": "3 Years", "image": "RG-ES05F.jpeg"},
            {"model": "RG-ES08G-L", "description": "8-Port Gigabit unmanaged Switch, 8 Gigabit RJ45 Ports, Plastic Case", "si_price": "2,880.00", "msrp": "3,460.00", "warranty": "3 Years", "image": "RG-ES05G-L.jpeg"},
            {"model": "RG-ES105GD", "description": "5-Port Gigabit unmanaged Switch, Steel Case", "si_price": "3,230.00", "msrp": "3,880.00", "warranty": "3 Years", "image": "RG-ES105GD.jpeg"},
            {"model": "RG-ES106F-P", "description": "6-Port 100Mbps, 4 PoE/PoE+ Ports, 54W PoE Budget, Steel Case", "si_price": "4,580.00", "msrp": "5,500.00", "warranty": "3 Years", "image": "RG-ES106F-P.jpeg"},
            {"model": "RG-ES108GD", "description": "8-Port Gigabit unmanaged Switch, Steel Case", "si_price": "4,310.00", "msrp": "5,170.00", "warranty": "3 Years", "image": "RG-ES108GD.jpeg"},
            {"model": "RG-ES110F-P", "description": "10-Port 100Mbps, 8 PoE/PoE+ Ports, 110W PoE Budget", "si_price": "8,400.00", "msrp": "10,080.00", "warranty": "3 Years", "image": "RG-ES110F-P.png"},
            {"model": "RG-ES110FG-P", "description": "8-Port 100Mbps + 2 Uplink 1000Mbps, 110W PoE Budget", "si_price": "11,950.00", "msrp": "14,330.00", "warranty": "3 Years", "image": "RG-ES110FG-P.png"},
            {"model": "RG-ES110GS-P-L", "description": "8-Port Gigabit + 1 RJ45 + 1 SFP Uplink, 120W PoE Budget", "si_price": "15,200.00", "msrp": "18,240.00", "warranty": "3 Years", "image": "RG-ES110GS-P-L.jpeg"},
            {"model": "RG-ES116G-L", "description": "16-Port Gigabit unmanaged Switch, Steel Case", "si_price": "10,150.00", "msrp": "12,180.00", "warranty": "3 Years", "image": "RG-ES116G-L.jpeg"},
            {"model": "RG-ES118FGS-LP", "description": "16-Port 100Mbps + 2 Combo Ports, 120W PoE Budget", "si_price": "20,890.00", "msrp": "25,070.00", "warranty": "3 Years", "image": "RG-ES118FGS-LP.jpeg"},
            {"model": "RG-ES118GS-P-L", "description": "16-Port Gigabit + 2 SFP, 247W PoE Budget", "si_price": "27,430.00", "msrp": "32,920.00", "warranty": "3 Years", "image": "RG-ES118GS-P-L.jpeg"},
            {"model": "RG-ES124G-L", "description": "24-Port Gigabit unmanaged Switch", "si_price": "12,970.00", "msrp": "15,560.00", "warranty": "3 Years", "image": "RG-ES124G-L.png"},
            {"model": "RG-ES126FGS-LP", "description": "24-Port 100Mbps + Combo Ports, 180W PoE Budget", "si_price": "26,480.00", "msrp": "31,770.00", "warranty": "3 Years", "image": "RG-ES126FGS-LP.jpeg"},
            {"model": "RG-ES126FGS-P", "description": "24-Port 100Mbps + Combo Ports, 370W PoE Budget", "si_price": "32,160.00", "msrp": "38,600.00", "warranty": "3 Years", "image": "RG-ES126FGS-P.png"},


            {"model": "RG-ES205GC", "description": "5-Port Gigabit Cloud Managed Switch", "si_price": "4,130.00", "msrp": "5,160.00", "warranty": "3 Years", "image": "RG-ES205GC.png"},
            {"model": "RG-ES205GC-P", "description": "5-Port Gigabit Smart PoE Switch, 54W Budget", "si_price": "9,430.00", "msrp": "11,790.00", "warranty": "3 Years", "image": "RG-ES205GC-P.png"},
            {"model": "RG-ES206GS-P", "description": "6-Port Gigabit Smart PoE Switch, 54W Budget", "si_price": "10,720.00", "msrp": "13,400.00", "warranty": "3 Years", "image": "RG-ES206GS-P.jpeg"},
            {"model": "RG-ES206MG-P", "description": "4-Port 2.5G PoE+ Cloud Managed Switch, 70W", "si_price": "20,570.00", "msrp": "25,720.00", "warranty": "3 Years", "image": "RG-ES206MG-P.jpeg"},
            {"model": "RG-ES208GC", "description": "8-Port Gigabit Cloud Managed Switch", "si_price": "5,080.00", "msrp": "6,350.00", "warranty": "3 Years", "image": "RG-ES208GC.jpeg"},
            {"model": "RG-ES209GC-P", "description": "9-Port Gigabit Smart PoE Switch, 120W Budget", "si_price": "16,680.00", "msrp": "20,850.00", "warranty": "3 Years", "image": "RG-ES209GC-P.jpeg"},
            {"model": "RG-ES209MG-P", "description": "8-Port 2.5G PoE+ Cloud Managed Switch, 130W", "si_price": "28,720.00", "msrp": "35,900.00", "warranty": "3 Years", "image": "RG-ES209MG-P.jpeg"},
            {"model": "RG-ES210GS-P", "description": "10-Port Gigabit Smart PoE Switch, 120W Budget", "si_price": "17,490.00", "msrp": "21,860.00", "warranty": "3 Years", "image": "RG-ES210GS-P.jpeg"},
            {"model": "RG-ES216GC-V2", "description": "16-Port Gigabit Smart Switch", "si_price": "16,180.00", "msrp": "20,220.00", "warranty": "3 Years", "image": "RG-ES216GC-V2.jpeg"},
            {"model": "RG-ES220GS-LP", "description": "16-Port Gigabit PoE+ Cloud Managed Switch", "si_price": "27,280.00", "msrp": "34,100.00", "warranty": "3 Years", "image": "RG-ES220GS-LP.png"},
            {"model": "RG-ES220GS-P", "description": "20-Port Gigabit Smart PoE Switch, 250W", "si_price": "35,240.00", "msrp": "44,040.00", "warranty": "3 Years", "image": "RG-ES220GS-P.jpeg"},
            {"model": "RG-ES224GC-V2", "description": "24-Port Gigabit Smart Switch", "si_price": "20,800.00", "msrp": "26,000.00", "warranty": "3 Years", "image": "RG-ES224GC-V2.jpeg"},
            {"model": "RG-ES228GS-LP", "description": "24-Port Gigabit PoE+ Cloud Managed Switch, 250W", "si_price": "37,190.00", "msrp": "46,490.00", "warranty": "3 Years", "image": "RG-ES228GS-LP.png"},
            {"model": "RG-ES228GS-P", "description": "28-Port Gigabit Smart PoE Switch, 370W", "si_price": "48,990.00", "msrp": "61,230.00", "warranty": "3 Years", "image": "RG-ES228GS-P.jpeg"},

            
            {"model": "RG-NBS3100-24GT4SFP-P-V2", "description": "24-Port Gigabit L2 Managed PoE Switch, 370W", "si_price": "57,980.00", "msrp": "72,480.00", "warranty": "5 Years", "image": "RG-NBS3100-24GT4SFP-P-V2.jpeg"},
            {"model": "RG-NBS3100-24GT4SFP-V2", "description": "24-Port Gigabit L2 Managed Switch", "si_price": "28,880.00", "msrp": "36,090.00", "warranty": "5 Years", "image": "RG-NBS3100-24GT4SFP-V2.jpeg"},
            {"model": "RG-NBS3100-48GT4SFP-P", "description": "48-Port Gigabit L2 Managed PoE Switch, 370W", "si_price": "112,120.00", "msrp": "140,150.00", "warranty": "5 Years", "image": "RG-NBS3100-48GT4SFP-P.png"},
            {"model": "RG-NBS3100-8GT2SFP", "description": "8-Port Gigabit L2 Managed Switch", "si_price": "19,480.00", "msrp": "24,350.00", "warranty": "5 Years", "image": "RG-NBS3100-8GT2SFP.jpeg"},
            {"model": "RG-NBS3100-8GT2SFP-P-V2", "description": "8-Port Gigabit L2 Managed PoE Switch, 125W", "si_price": "32,460.00", "msrp": "40,580.00", "warranty": "5 Years", "image": "RG-NBS3100-8GT2SFP-P-V2.jpeg"},
            {"model": "RG-EG105G-P-V3", "description": "5-Port Gigabit Cloud-Managed Router with 4 PoE Ports, 54W Budget", "si_price": "15,320.00", "msrp": "19,140.00", "warranty": "3 Years", "image": "RG-EG105G-P-V3.jpeg"},
            {"model": "RG-EG105G-V3", "description": "5-Port Gigabit Cloud-Managed Router", "si_price": "13,230.00", "msrp": "16,540.00", "warranty": "3 Years", "image": "RG-EG105G-V3.jpeg"},
            {"model": "RG-EG105GW(T)", "description": "All-in-One Enterprise Wireless Router with Mesh Support", "si_price": "13,960.00", "msrp": "17,440.00", "warranty": "3 Years", "image": "RG-EG105GW(T).png"},
            {"model": "RG-EG209GS", "description": "9-Port Cloud Management Router with SFP Port", "si_price": "14,710.00", "msrp": "18,390.00", "warranty": "3 Years", "image": "RG-EG209GS.png"},
            {"model": "RG-EG210G-P-V3", "description": "10-Port Gigabit Cloud-Managed Gateway with 8 PoE Ports, 110W Budget", "si_price": "24,840.00", "msrp": "31,040.00", "warranty": "3 Years", "image": "RG-EG210G-P-V3.jpeg"},
            {"model": "RG-EST100-E", "description": "2.4GHz Dual-Stream 500m Wireless Bridge, 300Mbps", "si_price": "7,650.00", "msrp": "9,560.00", "warranty": "3 Years", "image": "RG-EST100-E.png"},
            {"model": "RG-EST310 V2", "description": "5GHz Outdoor Wireless Bridge, 867Mbps, 10dBi Antenna", "si_price": "18,240.00", "msrp": "22,800.00", "warranty": "3 Years", "image": "RG-EST310_V2.jpeg"},
            {"model": "RG-EST330F-P", "description": "5GHz Wireless Bridge, 867Mbps, 3KM Transmission", "si_price": "11,270.00", "msrp": "14,080.00", "warranty": "3 Years", "image": "RG-EST330F-P.jpeg"},
            {"model": "RG-EST350G", "description": "5GHz Wireless Bridge, 5KM Long Distance, 16dBi Antenna", "si_price": "25,860.00", "msrp": "32,330.00", "warranty": "3 Years", "image": "RG-EST350G.jpeg"},
            {"model": "RG-EST450G", "description": "5GHz Wireless Bridge Base Station, 120° Antenna", "si_price": "18,290.00", "msrp": "22,860.00", "warranty": "3 Years", "image": "RG-EST450G.png"},
            {"model": "RG-E-120(GE)", "description": "1-Port PoE Adapter (802.3af)", "si_price": "3,900.00", "msrp": "4,880.00", "warranty": "3 Years", "image": "RG-E-120(GE).jpeg"},
            {"model": "RG-E-130(GE)", "description": "1-Port PoE Adapter (802.3at / PoE+)", "si_price": "4,740.00", "msrp": "5,930.00", "warranty": "3 Years", "image": "RG-E-130(GE).jpeg"},
            {"model": "RG-RAP1200(P)-MNT", "description": "Universal Mount Kit for RAP1200(P)", "si_price": "3,650.00", "msrp": "4,560.00", "warranty": "3 Years", "image": "RG-RAP1200(P)-MNT.jpeg"},
            {"model": "RG-POE-50-60W-MG", "description": "1-Port PoE Adapter (60W)", "si_price": "5,150.00", "msrp": "6,440.00", "warranty": "3 Years", "image": "RG-POE-50-60W-MG.jpeg"},
            {"model": "RG-POE-AF15", "description": "1-Port PoE Adapter (15.6W)", "si_price": "2,150.00", "msrp": "2,680.00", "warranty": "3 Years", "image": "RG-POE-AF15.jpeg"},
            {"model": "RG-POE-AT30", "description": "1-Port PoE Adapter (31.2W)", "si_price": "3,250.00", "msrp": "4,070.00", "warranty": "3 Years", "image": "RG-POE-AT30.jpeg"},
            {"model": "RG-RAP1200(F)", "description": "AC1300 Dual Band Wall Access Point", "si_price": "6,590.00", "msrp": "8,240.00", "warranty": "3 Years", "image": "RG-RAP1200(F).jpeg"},
            {"model": "RG-RAP1201", "description": "AC1300 Dual Band Wall Access Point, Gigabit Port", "si_price": "8,470.00", "msrp": "10,580.00", "warranty": "3 Years", "image": "RG-RAP1201.png"},
            {"model": "RG-RAP2200(E)", "description": "AC1300 Dual Band Ceiling Mount Access Point", "si_price": "12,980.00", "msrp": "16,230.00", "warranty": "3 Years", "image": "RG-RAP2200(E).webp"},
            {"model": "RG-RAP2200(F)", "description": "AC1300 Dual Band Ceiling Mount Access Point (100Base-T)", "si_price": "10,010.00", "msrp": "12,510.00", "warranty": "3 Years", "image": "RG-RAP2200(F).jpeg"},
            {"model": "RG-RAP2260(G)", "description": "AX1800 Dual Band Wi-Fi 6 Ceiling Access Point", "si_price": "18,350.00", "msrp": "22,940.00", "warranty": "3 Years", "image": "RG-RAP2260(G).jpeg"},
            {"model": "RG-RAP52-OD", "description": "AC1300 Outdoor Access Point, IP65", "si_price": "15,760.00", "msrp": "19,700.00", "warranty": "3 Years", "image": "RG-RAP52-OD.jpeg"},
            {"model": "RG-RAP62", "description": "Wi-Fi 6 AX1800 Dual-Band Ceiling Access Point", "si_price": "17,570.00", "msrp": "21,960.00", "warranty": "3 Years", "image": "RG-RAP62.png"},
            {"model": "RG-RAP6202(G)", "description": "AC1300 Outdoor Access Point, IP68", "si_price": "21,690.00", "msrp": "27,110.00", "warranty": "3 Years", "image": "RG-RAP6202(G).jpeg"},

            {"model": "RG-EW1200", "description": "1200M Dual-Band Wireless Home Router", "si_price": "3,680.00", "msrp": "4,230.00", "warranty": "3 Years", "image": "RG-EW1200.jpeg"},
            {"model": "RG-EW1200G PRO", "description": "1300M Dual-Band Gigabit Wireless Router", "si_price": "6,270.00", "msrp": "7,210.00", "warranty": "3 Years", "image": "RG-EW1200G_PRO.jpeg"},
            {"model": "RG-EW1300G", "description": "AC1300 Wi-Fi 5 Dual-Band Wireless Router", "si_price": "5,360.00", "msrp": "6,160.00", "warranty": "3 Years", "image": "RG-EW1300G.jpeg"},
            {"model": "RG-EW300 PRO", "description": "300Mbps Wireless Router, 4 Antennas", "si_price": "2,940.00", "msrp": "3,370.00", "warranty": "3 Years", "image": "RG-EW300_PRO.jpeg"},
            {"model": "RG-EW3000GX", "description": "AX3000 Dual-Band Wi-Fi 6 Router", "si_price": "9,680.00", "msrp": "11,130.00", "warranty": "3 Years", "image": "RG-EW3000GX.jpeg"},
            {"model": "RG-EW3000GX PRO", "description": "AX3000 Wi-Fi 6 Gaming Router", "si_price": "12,630.00", "msrp": "14,530.00", "warranty": "3 Years", "image": "RG-EW3000GX_PRO.jpeg"},
            {"model": "RG-EW300N", "description": "N300 Wi-Fi 4 Wireless Router", "si_price": "2,070.00", "msrp": "2,370.00", "warranty": "3 Years", "image": "RG-EW300N.jpeg"},
            {"model": "RG-EW6000GX", "description": "AX6000 Wi-Fi 6 Mesh Router", "si_price": "17,020.00", "msrp": "19,570.00", "warranty": "3 Years", "image": "RG-EW6000GX.jpeg"},
            {"model": "RG-M18", "description": "1800M Wi-Fi 6 Dual-Band Gigabit Mesh Router", "si_price": "14,620.00", "msrp": "16,810.00", "warranty": "3 Years", "image": "RG-M18.png"},
            {"model": "RG-M18(2PACK)", "description": "1800M Wi-Fi 6 Dual-Band Mesh Router (2 Pack)", "si_price": "24,770.00", "msrp": "28,490.00", "warranty": "3 Years", "image": "RG-M18(2PACK).jpeg"},
            {"model": "RG-M32", "description": "3200M Wi-Fi 6 Dual-Band Gigabit Mesh Router", "si_price": "23,780.00", "msrp": "27,350.00", "warranty": "3 Years", "image": "RG-M32.jpeg"},
            {"model": "RG-EW1200R", "description": "1200Mbps Dual-Band Mesh Wi-Fi Extender", "si_price": "4,590.00", "msrp": "5,270.00", "warranty": "3 Years", "image": "RG-EW1200R.jpeg"},
            {"model": "RG-EW300R", "description": "300Mbps Wi-Fi Extender", "si_price": "2,800.00", "msrp": "3,220.00", "warranty": "3 Years", "image": "RG-EW300R.jpeg"},

            
             # =============================
            # DINSTAR PRODUCTS (JAN 2026)
            # =============================

            
            {"model":"H60P","description":"Hotel IP Phone","msrp":"9600","image":"H60P.png"},
            {"model":"C60SP","description":"IP Phone (2 SIP Accounts, PoE)","msrp":"9600","image":"C60SP.jpeg"},
            {"model":"C60S","description":"IP Phone (2 SIP Accounts)","msrp":"9600","image":"C60S.jpeg"},
            {"model":"C60UP","description":"IP Phone with Backlight Display & PoE","msrp":"10420","image":"C60UP.png"},
            {"model":"C60U","description":"IP Phone with Backlight Display","msrp":"10420","image":"C60U.jpeg"},
            {"model":"C60UP-T","description":"4G LTE IP Phone","msrp":"21510","image":"C60UP-T.jpeg"},
            {"model":"C60U-W","description":"WiFi IP Phone","msrp":"13300","image":"C60U-W.png"},
            {"model":"C62UP","description":"Color Display IP Phone (6 SIP, PoE)","msrp":"13970","image":"C62UP.jpeg"},
            {"model":"C62U","description":"Color Display IP Phone (6 SIP)","msrp":"13970","image":"C62U.jpeg"},
            {"model":"C63GP","description":"Color Display IP Phone (30 Line Keys, PoE)","msrp":"16410","image":"C63GP.jpeg"},
            {"model":"C63G","description":"Color Display IP Phone (30 Line Keys)","msrp":"16410","image":"C63G.png"},
            {"model":"C64GP","description":"Executive IP Phone (16 SIP, PoE)","msrp":"23500","image":"C64GP.jpeg"},
            {"model":"C64G","description":"Executive IP Phone (16 SIP)","msrp":"23500","image":"C64G.png"},
            {"model":"C66GP","description":"High-End IP Phone (20 SIP, PoE)","msrp":"30150","image":"C66GP.jpeg"},
            {"model":"C66G","description":"High-End IP Phone (20 SIP)","msrp":"30150","image":"C66G.jpeg"},
            {"model":"DXP60","description":"Expansion Module (60 Programmable Keys)","msrp":"30150","image":"DXP60.jpeg"},
            {"model":"PSU","description":"Power Supply (EU/US/UK Standard)","msrp":"1040","image":"PSU.jpeg"},
            {"model":"WB11","description":"WiFi & Bluetooth Dongle","msrp":"4970","image":"WB11.jpeg"},

            {"model":"UC200-Pro-60","description":"UC200 Pro (60 SIP Users, 15 Calls)","msrp":"42570","image":"UC200-Pro-60.jpeg"},
            {"model":"UC200-Pro-200","description":"UC200 Pro (200 SIP Users, 30 Calls)","msrp":"58980","image":"UC200-Pro-200.png"},
            {"model":"UC200-Pro-500","description":"UC200 Pro (500 SIP Users, 50 Calls)","msrp":"87800","image":"UC200-Pro-500.png"},
            {"model":"UC350-500","description":"UC350 (500 SIP Users)","msrp":"186260","image":"UC350-500.jpeg"},
            {"model":"UC350-800","description":"UC350 (800 SIP Users)","msrp":"283800","image":"UC350-800.jpeg"},
            {"model":"UC350-1000","description":"UC350 (1000 SIP Users)","msrp":"350340","image":"UC350-1000.png"},
            {"model":"UC350PRO-2000","description":"UC350 Pro (2000 SIP Users)","msrp":"634160","image":"UC350PRO-2000.jpeg"},
            {"model":"UC350PRO-3000","description":"UC350 Pro (3000 SIP Users)","msrp":"749450","image":"UC350PRO-3000.png"},
            {"model":"UC350PRO-4000","description":"UC350 Pro (4000 SIP Users)","msrp":"862540","image":"UC350PRO-4000.jpeg"},
            {"model":"UC350PRO-5000","description":"UC350 Pro (5000 SIP Users)","msrp":"975620","image":"UC350PRO-5000.png"},

            {"model":"DAG1000-2S","description":"VoIP FXS Gateway (2 FXS)","msrp":"11970","image":"DAG1000-2S.jpeg"},
            {"model":"DAG1000-1S1O","description":"VoIP Gateway (1 FXS + 1 FXO)","msrp":"17740","image":"DAG1000-1S1O.jpeg"},
            {"model":"DAG1000-2O","description":"VoIP FXO Gateway (2 FXO)","msrp":"23500","image":"DAG1000-2O.jpeg"},
            {"model":"DAG1000-4S","description":"VoIP FXS Gateway (4 FXS)","msrp":"21730","image":"DAG1000-4S.jpeg"},
            {"model":"DAG1000-2S2O","description":"VoIP Gateway (2 FXS + 2 FXO)","msrp":"31490","image":"DAG1000-2S2O.jpeg"},
            {"model":"DAG1000-4O","description":"VoIP FXO Gateway (4 FXO)","msrp":"38580","image":"DAG1000-4O.png"},
            {"model":"DAG1000-8S","description":"VoIP FXS Gateway (8 FXS)","msrp":"43900","image":"DAG1000-8S.jpeg"},
            {"model":"DAG1000-8O","description":"VoIP FXO Gateway (8 FXO)","msrp":"65190","image":"DAG1000-8O.png"},
            {"model":"DAG1000-4S4O","description":"VoIP Gateway (4 FXS + 4 FXO)","msrp":"59870","image":"DAG1000-4S4O.png"},
            {"model":"DAG2000-16S","description":"VoIP FXS Gateway (16 FXS)","msrp":"72730","image":"DAG2000-16S.png"},
            {"model":"DAG2000-16O","description":"VoIP FXO Gateway (16 FXO)","msrp":"121950","image":"DAG2000-16O.jpeg"},
            {"model":"DAG2000-8S8O","description":"VoIP Gateway (8 FXS + 8 FXO)","msrp":"114410","image":"DAG2000-8S8O.png"},
            {"model":"DAG2000-24S","description":"VoIP FXS Gateway (24 FXS)","msrp":"108650","image":"DAG2000-24S.png"},
            {"model":"DAG2000-32S","description":"VoIP FXS Gateway (32 FXS)","msrp":"137920","image":"DAG2000-32S.png"},
            {"model":"DAG2500-48S","description":"VoIP FXS Gateway (48 FXS)","msrp":"231490","image":"DAG2500-48S.png"},
            {"model":"DAG2500-72S","description":"VoIP FXS Gateway (72 FXS)","msrp":"334820","image":"DAG2500-72S.png"},
            {"model":"DAG2500-96S","description":"VoIP FXS Gateway (96 FXS)","msrp":"446570","image":"DAG2500-96S.png"},
            {"model":"DAG3000-32S","description":"VoIP Gateway (32 FXS, 1U)","msrp":"246120","image":"DAG3000-32S.png"},
            {"model":"DAG3000-32O","description":"VoIP Gateway (32 FXO, 1U)","msrp":"313530","image":"DAG3000-32O.png"},
            {"model":"DAG3000-128S","description":"VoIP Gateway (128 FXS, 3U)","msrp":"605770","image":"DAG3000-128S.jpeg"},
            {"model":"DAG3000-128O","description":"VoIP Gateway (128 FXO, 3U)","msrp":"875400","image":"DAG3000-128O.png"},
            {"model":"DAG3000-312S","description":"High Density VoIP Gateway (312 FXS)","msrp":"1183610","image":"DAG3000-312S.jpeg"},



            # =============================
            # CNCOB PRODUCTS
            # =============================

            {"model": "COB-64069001","description": "6U wall mount cabinet, 600x450x368mm with tempered glass locking door and removable side doors","msrp": "12400","image": "COB-64069001.webp"},
            {"model": "COB-64099001","description": "9U wall mount cabinet, 600x450x501mm with tempered glass locking door and removable side doors","msrp": "17200","image": "COB-64099001.jpeg"},
            {"model": "COB-68279801","description": "27U 600x800 cabinet with 4 cooling fans (UK plug), vented doors","msrp": "70000","image": "COB-68279801.jpeg"},
            {"model": "COB-68429801","description": "42U 600x800 cabinet with 4 cooling fans (UK plug), vented doors","msrp": "105000","image": "COB-68429801.jpeg"},
            {"model": "COB-PC24005", "description": "CAT6 UTP patch cord with molded boots, 0.5M", "msrp": "180", "image": "COB-PC24005.jpeg"},
            {"model": "COB-PC24010","description": "CAT6 UTP patch cord with molded boots, 1M","msrp": "240", "image": "COB-PC24010.jpeg"},
            {"model": "COB-PC24020","description": "CAT6 UTP patch cord with molded boots, 2M","msrp": "310","image": "COB-PC24020.jpeg"},
            {"model": "COB-PC24030","description": "CAT6 UTP patch cord with molded boots, 3M","msrp": "410","image": "COB-PC24030.jpeg"},
            {"model": "COB-BC01","description": "CAT6 UTP solid cable, pure copper 0.55mm, 305m pulling box","msrp": "22500","image": "COB-BC01.jpeg"},
            {"model": "COB-BC02","description": "Outdoor CAT6 UTP solid cable, black PE jacket, 305m wood drum","msrp": "30000","image": "COB-BC02.jpeg"},
            {"model": "50724311000","description": "19” 1U 24 Ports CAT6 UTP Loaded Patch Panel","msrp": "7000","image": "50724311000.jpeg"},
            { "model": "10100510303","description": "CAT6 RJ45 connector (100 pcs), gold-plated contacts","msrp": "1000","image": "10100510303.jpeg"},
            {"model": "501033","description": "6P6C + 8P8C Crimping tool (3-in-1 tool)","msrp": "2400","image": "501033.jpeg"},
            {"model": "410023","description": "Smart portable network cable tester with 9V battery","msrp": "1000","image": "410023.jpeg"},
            {"model": "DUB-UK-67602", "description": "6 Universal Outlet Aluminium Rack Mount PDU, UK Plug","msrp": "4000","image": "DUB-UK-67602.jpeg"},
            {"model": "COB-CM010","description": "19” 1U 12 Slots Cable Management (Black)","msrp": "1400","image": "COB-CM010.jpeg"},
            {"model": "COB-FP003","description": "CAT6 faceplate with keystone jack, single port","msrp": "340","image": "COB-FP003.jpeg"},
            { "model": "COB-FP003-COMM", "description": "Communication faceplate with keystone jack, single port", "msrp": "310", "image": "COB-FP003-COMM.jpeg"},

        ]

        # 🔎 Get search query
        query = self.request.GET.get("q")

        if query:
            products = [
                p for p in products
                if query.lower() in p["model"].lower()
            ]

        # Remove `si_price` from every product dict (some entries include it).
        for p in products:
            p.pop("si_price", None)

        ctx["products"] = products
        ctx["query"] = query

        return ctx




# for certificat generator page

# for certificate generator page

import os
import subprocess
import tempfile
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView
from pptx import Presentation
from datetime import datetime
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin

class Certificate_GeneratorView(LoginRequiredMixin, TemplateView):
    template_name = "core/certificate_generator.html"
    login_url = '/login/'  # Redirect here if user is not logged in
    redirect_field_name = 'next'  # Optional: default is 'next'

    def post(self, request, *args, **kwargs):

        certificate_type = request.POST.get("certificate_type")

        if certificate_type == "internship_certificate":

            certificate_pptx_file_name = "internship_certificate_template.pptx"

            name = request.POST.get("name")
            position = format_with_article(request.POST.get("position"))
            from_date = format_date(request.POST.get("from_date"))
            to_date = format_date(request.POST.get("to_date"))

            replacements = {
                "{{name}}": name,
                "{{position}}": position,
                "{{from_date}}": from_date,
                "{{to_date}}": to_date,
            }

            return edit_certificate_and_download(certificate_pptx_file_name, replacements)


        elif certificate_type == "employment_certificate":

            certificate_pptx_file_name = "employment_certificate_template.pptx"

            name = request.POST.get("name")
            position = format_with_article(request.POST.get("position"))
            from_date = format_date(request.POST.get("from_date"))
            to_date = format_date(request.POST.get("to_date"))

            replacements = {
                "{{name}}": name,
                "{{position}}": position,
                "{{from_date}}": from_date,
                "{{to_date}}": to_date,
            }

            return edit_certificate_and_download(certificate_pptx_file_name, replacements)


        elif certificate_type == "course_certificate":

            certificate_pptx_file_name = "course_certificate_template.pptx"

            name = request.POST.get("name")
            course_name = request.POST.get("course_name")
            course_outcome = request.POST.get("course_outcome")
            from_date = format_date(request.POST.get("from_date"))
            to_date = format_date(request.POST.get("to_date"))
            training_hours = request.POST.get("training_hours")
            commitment_to = request.POST.get("commitment_to")

            course_coverage = format_course_coverage(
                json.loads(request.POST.get("course_coverage", "[]"))
            )

            replacements = {
                "{{name}}": name,
                "{{course_name}}": course_name,
                "{{course_outcome}}": course_outcome,
                "{{from_date}}": from_date,
                "{{to_date}}": to_date,
                "{{training_hours}}": training_hours,
                "{{course_coverage}}": course_coverage,
                "{{commitment_to}}": commitment_to,
            }

            return edit_certificate_and_download(certificate_pptx_file_name, replacements)

        return HttpResponse("Invalid certificate type")


def edit_certificate_and_download(certificate_pptx_file_name, replacements):

    template_path = os.path.join(
        settings.BASE_DIR,
        "core",
        "static",
        "core",
        certificate_pptx_file_name
    )

    prs = Presentation(template_path)

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue

            for paragraph in shape.text_frame.paragraphs:

                full_text = "".join(run.text for run in paragraph.runs)

                for key, value in replacements.items():
                    full_text = full_text.replace(key, value if value else "")

                if paragraph.runs:
                    paragraph.runs[0].text = full_text
                    for run in paragraph.runs[1:]:
                        run.text = ""

    with tempfile.TemporaryDirectory() as tmpdir:

        pptx_path = os.path.join(tmpdir, "certificate.pptx")
        prs.save(pptx_path)

        libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

        # subprocess.run([
        #     libreoffice_path,
        #     "--headless",
        #     "--convert-to", "png",
        #     pptx_path,
        #     "--outdir",
        #     tmpdir
        # ])

        result = subprocess.run([
            libreoffice_path,
            "--headless",
            "--convert-to",
            "png:draw_png_Export:Resolution=300,Width=3508,Height=2480",
            pptx_path,
            "--outdir",
            tmpdir
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        image_path = os.path.join(tmpdir, "certificate.png")

        # Check if conversion succeeded
        if not os.path.exists(image_path):
            print("LibreOffice Error:", result.stderr.decode())
            return HttpResponse("Certificate generation failed", status=500)

        with open(image_path, "rb") as f:
            image = f.read()

    # now preparing for sending the certificate generated via email
    # Current date & time
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")

    # Email
    subject = f"Certificate for {replacements.get('{{name}}')} - {now}"

    body = f"""
Hello,

Please find the certificate attached.

Name: {replacements.get('{{name}}')}
Generated on: {now}

Regards,
Certificate System
"""

    try:
        email_message = EmailMessage(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            settings.CERTIFICATE_RECIPIENT_EMAILS
        )

        email_message.attach("certificate.png", image, "image/png")

        email_message.send(fail_silently=False)

        return HttpResponse("Certificate sent to email successfully")

    except Exception as e:
        print("Email Error:", str(e))
        return HttpResponse("Failed to send certificate email", status=500)


# for previewer in certificate generator page
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def certificate_preview(request):

    if request.method != "POST":
        return HttpResponse(status=405)

    data = json.loads(request.body)

    certificate_type = data.get("certificate_type")

    if certificate_type == "internship_certificate":

        certificate_pptx_file_name = "internship_certificate_template.pptx"

        replacements = {
            "{{name}}": data.get("name", ""),
            "{{position}}": format_with_article(data.get("position", "")),
            "{{from_date}}": format_date(data.get("from_date", "")),
            "{{to_date}}": format_date(data.get("to_date", "")),
        }

    elif certificate_type == "employment_certificate":

        certificate_pptx_file_name = "employment_certificate_template.pptx"

        replacements = {
            "{{name}}": data.get("name", ""),
            "{{position}}": format_with_article(data.get("position", "")),
            "{{from_date}}": format_date(data.get("from_date", "")),
            "{{to_date}}": format_date(data.get("to_date", "")),
        }

    elif certificate_type == "course_certificate":

        certificate_pptx_file_name = "course_certificate_template.pptx"

        replacements = {
            "{{name}}": data.get("name", ""),
            "{{course_name}}": data.get("course_name", ""),
            "{{course_outcome}}": data.get("course_outcome", ""),
            "{{from_date}}": format_date(data.get("from_date", "")),
            "{{to_date}}": format_date(data.get("to_date", "")),
            "{{training_hours}}": data.get("training_hours", ""),
            "{{commitment_to}}": data.get("commitment_to", ""),

            "{{course_coverage}}": format_course_coverage(data.get("course_coverage", [])),

        }

    else:
        return HttpResponse("Invalid type", status=400)

    return generate_certificate_image(certificate_pptx_file_name, replacements)


def generate_certificate_image(template_name, replacements):

    template_path = os.path.join(
        settings.BASE_DIR,
        "core",
        "static",
        "core",
        template_name
    )

    prs = Presentation(template_path)

    for slide in prs.slides:
        for shape in slide.shapes:

            if not shape.has_text_frame:
                continue

            for paragraph in shape.text_frame.paragraphs:

                full_text = "".join(run.text for run in paragraph.runs)

                for key, value in replacements.items():
                    full_text = full_text.replace(key, value)

                if paragraph.runs:
                    paragraph.runs[0].text = full_text
                    for run in paragraph.runs[1:]:
                        run.text = ""

    with tempfile.TemporaryDirectory() as tmpdir:

        pptx_path = os.path.join(tmpdir, "preview.pptx")
        prs.save(pptx_path)

        libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

        result = subprocess.run([
            libreoffice_path,
            "--headless",
            "--convert-to",
            "png:draw_png_Export:Resolution=300,Width=3508,Height=2480",
            pptx_path,
            "--outdir",
            tmpdir
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        image_path = os.path.join(tmpdir, "preview.png")

        # Check if conversion succeeded
        if not os.path.exists(image_path):
            print("LibreOffice Error:", result.stderr.decode())
            return HttpResponse("Certificate Preview failed", status=500)

        with open(image_path, "rb") as f:
            image = f.read()

    return HttpResponse(image, content_type="image/png")



# Helper methods

def format_date(date):
    if date:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%B %d, %Y")
    else:
        return ""


def format_course_coverage(coverage_list):
    """
    Convert list of coverage topics into a single line string with bullets.
    """

    if not coverage_list:
        return ""

    if isinstance(coverage_list, str):
        try:
            coverage_list = json.loads(coverage_list)
        except:
            return coverage_list

    formatted = "   ".join([f"•{item}" for item in coverage_list])

    return formatted

def format_with_article(word: str) -> str:
    """
    Adds 'a' or 'an' before the word based on the starting vowel sound.
    """
    if not word:
        return ""
    
    # Check the first letter
    first_letter = word.strip()[0].lower()
    if first_letter in "aeiou":
        return f"an {word}"
    else:
        return f"a {word}"





# FOR VPS Page
class VPSView(TemplateView):
    template_name = 'core/vps.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["vps_categories"] = [
            {
                "category": "Starter VPS",
                "plans": [
                    {
                        "name": "Micro",
                        "image": "micro_vps.png",
                        "specs": {
                            "ram": "1 GB",
                            "storage": "30 GB SSD",
                            "cpu": "2 cores",
                            "ip": "Private IP",
                            "os": "Linux",
                        },
                        "price_monthly": "725",
                        "price_yearly": "7250",
                    },
                    {
                        "name": "Mini",
                        "image": "vps/mini.png",
                        "specs": {
                            "ram": "2 GB",
                            "storage": "40 GB SSD",
                            "cpu": "2 cores",
                            "ip": "Private IP",
                            "os": "Linux",
                        },
                        "price_monthly": "1025",
                        "price_yearly": "10250",
                    },
                ],
            },
            {
                "category": "Business VPS",
                "plans": [
                    {
                        "name": "Basic",
                        "image": "vps/basic.png",
                        "specs": {
                            "ram": "4 GB",
                            "storage": "50 GB SSD",
                            "cpu": "2 cores",
                            "ip": "Private IP",
                            "os": "Linux",
                        },
                        "price_monthly": "1460",
                        "price_yearly": "14600",
                    },
                    {
                        "name": "Standard",
                        "image": "vps/standard.png",
                        "specs": {
                            "ram": "6 GB",
                            "storage": "80 GB SSD",
                            "cpu": "4 cores",
                            "ip": "Shared Public IP",
                            "os": "Linux",
                        },
                        "price_monthly": "2200",
                        "price_yearly": "22000",
                    },
                ],
            },
            {
                "category": "Premium VPS",
                "plans": [
                    {
                        "name": "Premium",
                        "image": "vps/premium.png",
                        "specs": {
                            "ram": "8 GB",
                            "storage": "100 GB SSD",
                            "cpu": "8 cores",
                            "ip": "Dedicated Public IP",
                            "os": "Linux",
                        },
                        "price_monthly": "2900",
                        "price_yearly": "29000",
                    }
                ],
            },
        ]

        return ctx