import streamlit as st

st.set_page_config(layout="wide", )



c1, c2 = st.columns([4,8])
with c1:
    # st.image(
    #     "https://compass.uol/etc.clientlibs/compass/clientlibs/clientlib-react/resources/static/media/logo.d35fe3b1.svg",
    # )
    st.markdown("""
        <a href="https://compass.uol">
            <img class='img_increasse' src="https://compass.uol/etc.clientlibs/compass/clientlibs/clientlib-react/resources/static/media/logo.d35fe3b1.svg" alt="0" >
        </a>
        """, unsafe_allow_html=True)
with c2:
    st.markdown("# AS CHEIAS NO RIO GRANDE DO SUL")

# st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Lista de Abrigos", "Princiapis Impactos", "Frente de Ajuda", "Rio Grande em Números"])

with tab4:
    st.text("vamos la")

st.markdown("""
<style>
@media (min-width: 1162px) and (max-width: 4000px){
    .img_increasse {
        position: absolute;
        top: 60%;
        right: 15%;
    }
    div[data-testid='stMarkdownContainer'] {
        min-height: 200px;
    }
}
@media (min-width: 641px) and (max-width: 1161px){
    .img_increasse {
        position: absolute;
        top: 60%;
        right: 33%;
    }
    div[data-testid='stMarkdownContainer'] {
        min-height: 200px;
    }
}            
@media (min-width: 515px) and (max-width: 640px){
    .img_increasse {
        position: absolute;
        top: 60%;
        left: 33%;
    }
    div[data-testid='stMarkdownContainer'] {
        min-height: 0px;
    }
}
@media (min-width: 321px) and (max-width: 514px){
    .img_increasse {
        position: absolute;
        top: 60%;
        left: 25%;
    }
    div[data-testid='stMarkdownContainer'] {
        min-height: 0px;
    }
}
@media (min-width: 373px) and (max-width: 514px){
    .img_increasse {
        position: absolute;
        top: 60%;
        left: 25%;
    }
    div[data-testid='stMarkdownContainer'] {
        min-height: 0px;
    }
}
@media (min-width: 0px) and (max-width: 373px){
    .img_increasse {
        position: absolute;
        top: 60%;
        left: 10%;
    }
    div[data-testid='stMarkdownContainer'] {
        min-height: 0px;
    }
}
.st-emotion-cache-zt5igj {
    min-height: 200px;
}
.st-bd {
    color: #f1cf49;
}
.st-bs {
    line-height: 20;
}
.st-bs:hover {
    line-height: 20;
    color: #f1cf49;
}
.st-c2 {
    background-color: #f1cf49;
}
.st-bs:focus {
    color: #f1cf49;
}     
div[data-baseweb='tab-list']  {
    display: flex;
    justify-content: space-around;
}               
# .st-emotion-cache-imfc0n {
#     display: none;
# }
</style>
  

<script>
# var div = document.querySelectorAll('[data-test-id=column]');
# var children = div.childNodes; 
# var elements = []; 
# for (var i=0; i<div.childNodes.length; i++) { 
#   var child = div.childNodes[i]; 
#   if (child.nodeType == 1) { 
#     elements.push(child)       
#   } 
# }             
</script>
""", unsafe_allow_html=True)

