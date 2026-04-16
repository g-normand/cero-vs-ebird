<script setup>
import SpeciesCategory from './components/SpeciesCategory.vue'
import FooterInfo from './components/FooterInfo.vue'
import categories from "./assets/categories.json";
import logo_guiguide from "./assets/logo_guiguide.png";
import logo_zoziologie from "./assets/logo_zoziologie.svg";
</script>

<template>
  <div>

    <b-button squared v-b-toggle.sidebar-categories class="categories-button" v-show="show_sidebar_button">Ver categorías</b-button>
    <b-sidebar title="Categorías" shadow id="sidebar-categories" class="mt-2">
      <b-overlay rounded="sm">
          <div class="py-2" id="category-group">
          <b-button
            squared
            v-for="(r, i) in categories"
            :key="r.category"
            :class="r.code === current_category.code ? 'current-categories-button' : 'categories-button'"
            @click="changeCategory(r)">
            <b-icon icon="binoculars" />
            {{ r.name }}
          </b-button>
        </div>
      </b-overlay>
      <template #footer>
        <div class="d-flex bg-dark text-light align-items-center px-3 py-2 w-100 justify-content-between">
          Made with <b-icon icon="heart" /> by
          <a href="https://guiguide.alwaysdata.net/" target="_blank" title="guiguide.alwaysdata.net"
            ><b-img :src="logo_guiguide" class="zozio"></b-img>
          Guillaume Normand</a>
        </div>
        <div class="d-flex bg-dark text-light align-items-center px-3 py-2 w-100 justify-content-between">
          Inspired by 
          <a href="https://zoziologie.raphaelnussbaumer.com/see-your-observations/" target="_blank" title="zoziologie.com"
            ><b-img :src="logo_zoziologie" class="zozio"></b-img></a>
        </div>
      </template>
    </b-sidebar>
  </div>

  <SpeciesCategory :category=current_category />
  <FooterInfo />
</template>

<script>
export default {
  data() {
    return {
      logo_zoziologie: logo_zoziologie,
      logo_guiguide: logo_guiguide,
      categories: categories,
      current_category: "VU",
      show_sidebar_button: false,
    }
  },
  methods: {
    changeCategory(r) {
      this.current_category = r;
      if (window.innerWidth <= 760){
        this.$root.$emit('bv::toggle::collapse', 'sidebar-categories');
        this.show_sidebar_button = true;
      }
    }
  },
  mounted: function () {   
    if (window.innerWidth >= 760){
      // Show sidebar
      this.$root.$emit('bv::toggle::collapse', 'sidebar-categories');
      this.show_sidebar_button = true;
    }
    else{
      this.show_sidebar_button = false;
    }
  },
}


</script>
