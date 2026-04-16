<template>
<b-container fluid class="h-100 bg-light overflow-auto" id="specieslist">
  <b-row class="h-100">
    <b-col class="h-100 col-xs-12 md-9 col-lg-9 d-flex flex-column py-2">
       <b-card v-if="category.name">
        <b-card-body>
          <h3> {{ category.name }} ({{ category_list.length }})</h3>
          <b-table id="species_table"
            hover             
            responsive
            :fields="[
              { key: 'english_name', label: 'Especie', sortable: true },
              { key: 'notes', label: 'Nota', sortable: true },
              { key: 'ebird_checklist', label: 'Checklist', sortable: true },
            ]"
            :items="category_list"
            :per-page="perPage"
            :current-page="currentPage"
          >
            <template #cell(ebird_checklist)="sp">
              <b-link
                :href="sp.item.ebird_checklist" 
                target="_blank"
              >
                {{ sp.value }}
              </b-link>
           </template>
            <template #cell(english_name)="sp">
              <b-link
                :href="sp.item.species_code + '/EC'" 
                target="_blank"
              >
                {{ sp.value }}
              </b-link>
            </template>
            <template #cell(notes)="sp">
              <div v-html="sp.item.notes"></div>
            </template>
          </b-table>
           <b-pagination
              v-if="category_list.length > 50"
              v-model="currentPage"
              :total-rows="category_list.length"
              :per-page="perPage"
              align="center"
              class="my-2"
            />
        </b-card-body>
      </b-card>
      <b-card fluid class="h-100 bg-light" v-if="!category.name">
        <h3>CERO data vs eBird data</h3>
        Por favor, seleccione una categoría.<br />
        <b-button squared v-b-toggle.sidebar-categories class="categories-button" v-show="show_categories_button">Ver categorías</b-button>
      </b-card>
    </b-col>
  </b-row>
</b-container>
</template>
<script setup>
import { eventBus } from "../main";
import species_list from "../assets/species_list.json";
</script>

<script>
export default {
  data() {
    return {
      species_list: species_list,
      category_list: [],
      currentPage: 1,
      perPage:50,
      showIframes: true,  
      show_categories_button:false,
    }
  },
  props: ['category'],
  methods: {
    species_list_table() {
        this.category_list = this.species_list
          .filter((s) => s.category.includes(this.category.code));
        this.show_categories_button = false;
    }
  },
  created: function() {
    eventBus.$on("userdata-changed", (data) => {
      this.species_list_table();
    });
  },
  watch: { 
    category: function(newVal, oldVal) { // watch it
      this.currentPage = 1;
      this.species_list_table();
      this.showIframes = false;
      this.$nextTick(() => {
        this.showIframes = true;
      });
    },
    currentPage() {
      this.showIframes = false;
      this.$nextTick(() => {
        this.showIframes = true;
      });
    }
  },
  mounted: function () {   
    if (window.innerWidth <= 760){
      this.show_categories_button = true;
    }
  },
};

</script>