from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AS Security & Facility Services</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #080a0f;
    color: white;
    line-height: 1.6;
}

/* ================= NAVBAR ================= */

nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 999;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 12px 5%;

    background: rgba(5,7,10,0.96);
    backdrop-filter: blur(12px);

    border-bottom: 1px solid #252932;
}

.brand {
    display: flex;
    align-items: center;
    gap: 10px;
}

/* CSS LOGO */

.logo {
    width: 48px;
    height: 48px;

    border: 2px solid #d71920;
    border-radius: 50%;

    display: flex;
    justify-content: center;
    align-items: center;

    background: #ffffff;

    color: #18245c;

    font-size: 18px;
    font-weight: 900;

    font-style: italic;

    box-shadow: 0 0 15px rgba(215,25,32,0.25);
}

.brand-text {
    font-weight: bold;
    font-size: 14px;
    line-height: 1.1;
}

.brand-text span {
    color: #e21b23;
}

.nav-links {
    display: flex;
    gap: 18px;
}

.nav-links a {
    color: white;
    text-decoration: none;
    font-size: 13px;
}

.nav-links a:hover {
    color: #e21b23;
}


/* ================= HERO ================= */

.hero {
    min-height: 100vh;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;

    padding: 120px 20px 60px;

    background:
    radial-gradient(
        circle at top,
        rgba(215,25,32,0.18),
        transparent 40%
    ),
    linear-gradient(
        135deg,
        #090b10,
        #151923
    );
}

.hero-content {
    max-width: 850px;

    animation: fadeUp 1s ease;
}

/* BIG LOGO */

.big-logo {
    width: 125px;
    height: 125px;

    margin: 0 auto 25px;

    border: 4px solid #d71920;

    border-radius: 50%;

    background: white;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #18245c;

    font-size: 48px;

    font-weight: 900;

    font-style: italic;

    box-shadow:
    0 0 35px rgba(215,25,32,0.30);
}

.badge {
    display: inline-block;

    padding: 8px 18px;

    border: 1px solid #d71920;

    border-radius: 30px;

    color: #ff4a50;

    font-size: 12px;

    font-weight: bold;

    letter-spacing: 1px;

    margin-bottom: 20px;
}

.hero h1 {
    font-size: clamp(45px, 11vw, 82px);

    line-height: 1;

    font-weight: 900;

    letter-spacing: 2px;
}

.hero h1 span {
    color: #e21b23;
}

.hero h2 {
    margin-top: 15px;

    font-size: clamp(22px, 5vw, 36px);

    color: #eeeeee;
}

.hero p {
    max-width: 700px;

    margin: 22px auto;

    color: #aeb4bd;

    font-size: 16px;
}


/* ================= BUTTONS ================= */

.buttons {
    margin-top: 28px;
}

.btn {
    display: inline-block;

    padding: 14px 23px;

    margin: 6px;

    border-radius: 9px;

    text-decoration: none;

    font-weight: bold;

    transition: 0.3s;
}

.call {
    background: #d71920;
    color: white;

    box-shadow:
    0 8px 25px rgba(215,25,32,0.30);
}

.call:hover {
    transform: translateY(-4px);
    background: #f0262d;
}

.whatsapp {
    background: #168c3b;
    color: white;
}

.whatsapp:hover {
    transform: translateY(-4px);
    background: #20a84b;
}

.explore {
    border: 1px solid #555;
    color: white;
}

.explore:hover {
    border-color: #e21b23;
    transform: translateY(-4px);
}


/* ================= SECTIONS ================= */

section {
    padding: 85px 6%;
}

.section-title {
    text-align: center;
    margin-bottom: 45px;
}

.section-title h2 {
    font-size: 35px;
}

.section-title h2 span {
    color: #e21b23;
}

.section-title p {
    color: #9299a3;
    margin-top: 8px;
}


/* ================= ABOUT ================= */

.about {
    background: #0d1016;
}

.about-box {
    max-width: 900px;

    margin: auto;

    padding: 35px;

    background: #13171e;

    border: 1px solid #262c35;

    border-radius: 18px;

    text-align: center;
}

.about-box p {
    color: #c1c6cd;

    font-size: 15px;
}


/* ================= SERVICES ================= */

.services {
    background: #080a0f;
}

.cards {
    max-width: 1100px;

    margin: auto;

    display: grid;

    grid-template-columns:
    repeat(auto-fit, minmax(210px, 1fr));

    gap: 20px;
}

.card {
    background: #12161d;

    border: 1px solid #252b34;

    border-radius: 16px;

    padding: 28px 20px;

    text-align: center;

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-7px);

    border-color: #e21b23;
}

.icon {
    font-size: 38px;

    margin-bottom: 12px;
}

.card h3 {
    color: #ffffff;

    margin-bottom: 8px;
}

.card p {
    color: #9299a3;

    font-size: 14px;
}


/* ================= WHY ================= */

.why {
    background: #0d1016;
}

.highlights {
    max-width: 1100px;

    margin: auto;

    display: grid;

    grid-template-columns:
    repeat(auto-fit, minmax(180px, 1fr));

    gap: 18px;
}

.highlight {
    background: #14181f;

    border: 1px solid #252b34;

    border-radius: 15px;

    text-align: center;

    padding: 25px 15px;
}

.highlight strong {
    display: block;

    font-size: 30px;

    color: #e21b23;

    margin-bottom: 6px;
}

.highlight p {
    color: #aeb4bd;

    font-size: 14px;
}


/* ================= FOUNDERS ================= */

.founders {
    background: #080a0f;
}

.founder-container {
    max-width: 850px;

    margin: auto;

    display: grid;

    grid-template-columns:
    repeat(auto-fit, minmax(250px, 1fr));

    gap: 22px;
}

.founder {
    background: #12161d;

    border: 1px solid #252b34;

    border-radius: 18px;

    padding: 32px 22px;

    text-align: center;

    transition: 0.3s;
}

.founder:hover {
    transform: translateY(-6px);

    border-color: #e21b23;
}

.person {
    width: 70px;
    height: 70px;

    margin: auto;

    border-radius: 50%;

    background: rgba(215,25,32,0.12);

    border: 1px solid #d71920;

    display: flex;

    justify-content: center;
    align-items: center;

    font-size: 30px;
}

.founder h3 {
    margin-top: 17px;

    font-size: 20px;
}

.role {
    color: #e21b23;

    font-size: 12px;

    font-weight: bold;

    margin-top: 5px;

    letter-spacing: 1px;
}

.founder-phone {
    display: block;

    margin-top: 12px;

    color: #e21b23;

    font-size: 15px;

    font-weight: bold;

    text-decoration: none;
}

.founder-phone:hover {
    color: #ff4a50;

    text-decoration: underline;
}

.founder p {
    color: #9299a3;

    font-size: 14px;

    margin-top: 12px;
}


/* ================= SERVICE AREA ================= */

.area {
    background:
    linear-gradient(
        135deg,
        #11151c,
        #090b10
    );

    text-align: center;
}

.area-box {
    max-width: 850px;

    margin: auto;

    padding: 40px 20px;

    border: 1px solid #2a3039;

    border-radius: 20px;

    background: #11151b;
}

.area-big {
    font-size: 42px;

    font-weight: 900;

    color: #e21b23;
}

.area-box p {
    color: #aeb4bd;

    margin-top: 10px;
}


/* ================= CONTACT ================= */

.contact {
    background: #0d1016;

    text-align: center;
}

.contact-box {
    max-width: 850px;

    margin: auto;

    padding: 40px 25px;

    background: #13171e;

    border: 1px solid #272d36;

    border-radius: 20px;
}

.phone {
    font-size: 30px;

    font-weight: bold;

    color: white;

    margin: 10px;
}

.phone span {
    color: #e21b23;
}

.contact-item {
    color: #aeb4bd;

    margin: 18px 0;

    font-size: 15px;
}

.contact-item strong {
    color: white;
}


/* ================= FOOTER ================= */

footer {
    text-align: center;

    padding: 28px 20px;

    background: #050609;

    color: #6f7680;

    font-size: 13px;
}

footer strong {
    color: #e21b23;
}


/* ================= ANIMATION ================= */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(35px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }

}


/* ================= MOBILE ================= */

@media(max-width: 700px) {

    nav {
        padding: 10px 4%;
    }

    .logo {
        width: 42px;
        height: 42px;
        font-size: 15px;
    }

    .brand-text {
        font-size: 11px;
    }

    .nav-links {
        gap: 8px;
    }

    .nav-links a {
        font-size: 10px;
    }

    .hero {
        padding-top: 120px;
    }

    .big-logo {
        width: 105px;
        height: 105px;

        font-size: 40px;
    }

    section {
        padding: 70px 5%;
    }

    .section-title h2 {
        font-size: 29px;
    }

    .about-box {
        padding: 25px 18px;
    }

    .phone {
        font-size: 24px;
    }

    .area-big {
        font-size: 32px;
    }

}

</style>

</head>

<body>


<!-- ================= NAVIGATION ================= -->

<nav>

    <div class="brand">

        <div class="logo">
            AS
        </div>

        <div class="brand-text">
            AS<br>
            <span>SECURITY</span>
        </div>

    </div>


    <div class="nav-links">

        <a href="#home">Home</a>

        <a href="#services">Services</a>

        <a href="#about">About</a>

        <a href="#founders">Founders</a>

        <a href="#contact">Contact</a>

    </div>

</nav>


<!-- ================= HERO ================= -->

<section class="hero" id="home">

    <div class="hero-content">


        <div class="big-logo">
            AS
        </div>


        <div class="badge">
            PROFESSIONAL SECURITY & FACILITY SERVICES
        </div>


        <h1>
            AS <span>SECURITY</span>
        </h1>


        <h2>
            & Facility Services
        </h2>


        <p>
            Professional, reliable and responsible security
            solutions for residential, commercial,
            industrial and corporate requirements.
        </p>


        <div class="buttons">

            <a
            class="btn call"
            href="tel:9871351971">
                📞 Call 9871351971
            </a>


            <a
            class="btn whatsapp"
            href="https://wa.me/919871351971"
            target="_blank">
                💬 WhatsApp
            </a>


            <a
            class="btn explore"
            href="#services">
                Explore Services
            </a>

        </div>

    </div>

</section>


<!-- ================= ABOUT ================= -->

<section class="about" id="about">

    <div class="section-title">

        <h2>
            About <span>AS Security</span>
        </h2>

        <p>
            Professional. Reliable. Responsible.
        </p>

    </div>


    <div class="about-box">

        <p>
            <strong>
            AS Security & Facility Services
            </strong>
            provides professional security and facility
            support solutions for different types of
            residential, commercial and industrial
            requirements.
        </p>

        <br>

        <p>
            Our objective is to provide dependable,
            disciplined and client-focused security
            services while understanding the specific
            requirements of every location.
        </p>

        <br>

        <p>
            We serve clients across the
            <strong>Delhi NCR</strong> region.
        </p>

    </div>

</section>


<!-- ================= SERVICES ================= -->

<section class="services" id="services">

    <div class="section-title">

        <h2>
            Our <span>Services</span>
        </h2>

        <p>
            Security solutions for different requirements
        </p>

    </div>


    <div class="cards">


        <div class="card">

            <div class="icon">🛡️</div>

            <h3>
                Security Guards
            </h3>

            <p>
                Professional security personnel
                for people and property protection.
            </p>

        </div>


        <div class="card">

            <div class="icon">🏢</div>

            <h3>
                Corporate Security
            </h3>

            <p>
                Security support for offices
                and corporate premises.
            </p>

        </div>


        <div class="card">

            <div class="icon">🏠</div>

            <h3>
                Society Security
            </h3>

            <p>
                Security solutions for
                residential societies and apartments.
            </p>

        </div>


        <div class="card">

            <div class="icon">🏭</div>

            <h3>
                Industrial Security
            </h3>

            <p>
                Security support for factories,
                warehouses and industrial locations.
            </p>

        </div>


        <div class="card">

            <div class="icon">🏗️</div>

            <h3>
                Construction Security
            </h3>

            <p>
                Protection and security support
                for construction sites.
            </p>

        </div>


        <div class="card">

            <div class="icon">🚪</div>

            <h3>
                Gate Security
            </h3>

            <p>
                Professional entry and exit
                security management.
            </p>

        </div>


        <div class="card">

            <div class="icon">🌙</div>

            <h3>
                Night Security
            </h3>

            <p>
                Security support for locations
                requiring night protection.
            </p>

        </div>


        <div class="card">

            <div class="icon">⚙️</div>

            <h3>
                Facility Services
            </h3>

            <p>
                Facility support solutions
                according to client requirements.
            </p>

        </div>


    </div>

</section>


<!-- ================= WHY US ================= -->

<section class="why">

    <div class="section-title">

        <h2>
            Why Choose <span>AS Security?</span>
        </h2>

        <p>
            Security with professionalism and responsibility
        </p>

    </div>


    <div class="highlights">


        <div class="highlight">

            <strong>24/7</strong>

            <p>
                Security Support
            </p>

        </div>


        <div class="highlight">

            <strong>✓</strong>

            <p>
                Professional Approach
            </p>

        </div>


        <div class="highlight">

            <strong>✓</strong>

            <p>
                Reliable Service
            </p>

        </div>


        <div class="highlight">

            <strong>✓</strong>

            <p>
                Client Focused
            </p>

        </div>


        <div class="highlight">

            <strong>NCR</strong>

            <p>
                Service Coverage
            </p>

        </div>


    </div>

</section>


<!-- ================= FOUNDERS ================= -->

<section class="founders" id="founders">

    <div class="section-title">

        <h2>
            Our <span>Founders</span>
        </h2>

        <p>
            Leadership of AS Security & Facility Services
        </p>

    </div>


    <div class="founder-container">


        <!-- FOUNDER 1 -->

        <div class="founder">

            <div class="person">
                👤
            </div>

            <h3>
                Subhankar Chaudhary
            </h3>

            <div class="role">
                FOUNDER
            </div>

            <a
            class="founder-phone"
            href="tel:9871351971">
                📞 9871351971
            </a>

            <p>
                Focused on professional security
                services, operations and client
                satisfaction.
            </p>

        </div>


        <!-- FOUNDER 2 -->

        <div class="founder">

            <div class="person">
                👤
            </div>

            <h3>
                Anand Kumar
            </h3>

            <div class="role">
                CO-FOUNDER
            </div>

            <a
            class="founder-phone"
            href="tel:9910928639">
                📞 9910928639
            </a>

            <p>
                Supporting company operations
                and reliable service delivery.
            </p>

        </div>


    </div>

</section>


<!-- ================= SERVICE AREA ================= -->

<section class="area">

    <div class="section-title">

        <h2>
            Service <span>Area</span>
        </h2>

        <p>
            Serving clients across
        </p>

    </div>


    <div class="area-box">

        <div class="area-big">
            DELHI NCR
        </div>

        <p>
            Faridabad • Delhi • Noida • Gurugram
            • Greater Noida and surrounding NCR areas
        </p>

    </div>

</section>


<!-- ================= CONTACT ================= -->

<section class="contact" id="contact">

    <div class="section-title">

        <h2>
            Contact <span>Us</span>
        </h2>

        <p>
            For security and facility service enquiries
        </p>

    </div>


    <div class="contact-box">


        <div class="phone">

            📞 <span>9871351971</span>

        </div>


        <div class="contact-item">

            <strong>
                Company Address
            </strong>

            <br>

            H.No. 111, 45 Feet Road,
            Bharat Colony, Khedi Road,
            Sector-87,
            Faridabad-121002,
            Haryana

        </div>


        <div class="contact-item">

            <strong>
                Service Area
            </strong>

            <br>

            Delhi NCR

        </div>


        <div class="buttons">

            <a
            class="btn call"
            href="tel:9871351971">
                📞 Call Us
            </a>


            <a
            class="btn whatsapp"
            href="https://wa.me/919871351971"
            target="_blank">
                💬 WhatsApp Us
            </a>

        </div>


    </div>

</section>


<!-- ================= FOOTER ================= -->

<footer>

    © 2026

    <strong>
        AS Security & Facility Services
    </strong>

    <br>

    Professional Security & Facility Solutions
    | Delhi NCR

</footer>


</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )