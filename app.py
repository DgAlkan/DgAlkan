import streamlit as st
st.set_page_config(page_title="Analytics Intelligence Lab | Rodrigo Alcantara", page_icon="📊", layout="wide")
lang=st.sidebar.radio("Idioma / Language",["Português","English"])
def tr(pt,en):
    return pt if lang=="Português" else en
st.markdown("""<style>
.stApp{background:#f1f5f9}
[data-testid="stMainBlockContainer"]{max-width:1250px;padding-top:2rem}
.hero{background:linear-gradient(120deg,#0b1526,#193a60);border-radius:20px;padding:40px;color:white}
.hero h1{color:white;font-size:clamp(2rem,5vw,3.5rem);padding:8px 0}
.hero p{color:#cbd5e1;font-size:1.1rem}
.kicker{color:#7dd3fc;letter-spacing:2px;font-weight:bold}
[data-testid="stMetric"]{background:white;border:1px solid #dbe4ef;border-radius:14px;padding:16px}
</style>""",unsafe_allow_html=True)
st.markdown(f"""<section class="hero"><div class="kicker">ANALYTICS INTELLIGENCE LAB</div><h1>Rodrigo Alcantara</h1><p>Data Analytics &amp; Analytics Engineering</p><p>{tr("Transformando dados complexos em decisões confiáveis.","Turning complex data into reliable decisions.")}</p></section>""",unsafe_allow_html=True)
st.caption("Microsoft Certified: Fabric Analytics Engineer Associate · DP-600")
section=st.sidebar.radio(tr("Navegação","Navigation"),["Portfolio","Expertise", "About"],format_func=lambda x:tr({"Portfolio":"Projetos","Expertise":"Competências","About":"Sobre mim"}[x],x))
if section=="Portfolio":
    st.header(tr("Produtos analíticos","Analytics products"))
    st.write(tr("Explore demonstrações interativas com dados sintéticos. Cada produto conecta um problema de negócio a uma solução analítica reproduzível.","Explore interactive synthetic-data demos connecting business problems to reproducible analytical solutions."))
    products=[
        ("01 · DATA QUALITY","Data Reconciliation Engine",tr("Auditoria de migrações, comparação campo a campo e geração de evidências.","Migration audits, field-level comparisons and evidence generation."),"5,000",tr("Registros sintéticos de origem","Synthetic source records"),"dgalkan-data-quality","data-reconciliation-engine"),
        ("02 · DECISION SCIENCE","Decision Intelligence Platform",tr("Indicadores operacionais, análise de No-show e simulação de cenários.","Operational KPIs, no-show analysis and scenario simulation."),"100,000",tr("Agendamentos sintéticos","Synthetic appointments"),"dgalkan-decision-intelligence","decision-intelligence-plataform"),
        ("03 · CUSTOMER ANALYTICS","Customer Journey Intelligence",tr("Ciclo de vida, risco de inatividade e retenção por coortes.","Lifecycle, inactivity risk and cohort retention."),"5,000",tr("Clientes sintéticos","Synthetic customers"),"dgalkan-customer-journey","customer-journey-intelligence")]
    for col,p in zip(st.columns(3),products):
        with col:
            with st.container(border=True):
                st.caption(p[0])
                st.subheader(p[1])
                st.write(p[2])
                st.metric(p[4],p[3])
                st.caption(tr("Volume máximo configurado na demonstração","Maximum configured demo volume"))
                st.link_button(tr("Explorar aplicação","Launch application"),f"https://{p[5]}.streamlit.app",type="primary",use_container_width=True)
                st.markdown(f"[{tr('Repositório técnico (acesso restrito)','Technical repository (restricted access)')}](https://github.com/DgAlkan/{p[6]})")
    st.info(tr("Demonstrações independentes com dados sintéticos. Não envie informações pessoais ou corporativas.","Independent synthetic-data demonstrations. Never upload personal or corporate information."))
elif section=="Expertise":
    st.header(tr("Competências e tecnologia","Expertise and technology"))
    for title,body in [
        ("Analytics Engineering","SQL · Python · Pandas · DuckDB · Microsoft Fabric · Databricks · Amazon Redshift"),
        ("Business Intelligence","Power BI · DAX · Power Query · KPI design"),
        ("Data Quality",tr("Conciliação · Validação de regras · Evidências auditáveis","Reconciliation · Rule validation · Auditable evidence")),
        ("Product Engineering","Streamlit · Pytest · GitHub Actions · i18n")]:
        with st.container(border=True):
            st.subheader(title)
            st.write(body)
    st.subheader(tr("Arquitetura dos projetos","Project architecture"))
    st.code("Synthetic data → Python / SQL → Validation → Streamlit → Evidence export",language=None)
else:
    st.header(tr("Sobre mim","About me"))
    st.write(tr("Profissional de análise de dados com experiência em inteligência de negócios, modelagem analítica, qualidade de dados e automação de processos. Meu foco é conectar perguntas de negócio a dados confiáveis e decisões fundamentadas.","Data analytics professional experienced in business intelligence, analytical modeling, data quality and process automation. My focus is connecting business questions to reliable data and informed decisions."))
    st.subheader(tr("Certificação","Certification"))
    st.write("Microsoft Certified: Fabric Analytics Engineer Associate (DP-600)")
    st.subheader(tr("Princípios de trabalho","Working principles"))
    st.write(tr("Reprodutibilidade, qualidade, transparência metodológica e proteção de informações confidenciais.","Reproducibility, quality, methodological transparency and confidentiality."))
st.divider()
st.markdown("[GitHub · DgAlkan](https://github.com/DgAlkan)")
st.caption(tr("Portfólio independente. Resultados sintéticos não representam desempenho empresarial real.","Independent portfolio. Synthetic results do not represent actual business performance."))
