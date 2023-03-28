import unittest


from app.domain.repositories.component_repository import ComponentRepositoryInMemory as Reopository
from app.domain.entities.component import Component


class MyTest(unittest.TestCase):
    """
    unit test
    """

    def test_repository_add(self):
        """ repositoryにadd出来るかテスト
        """
        new_repo = Reopository()
        new_component = Component(id=0,
                                  component="""<template>
  <v-dialog v-model="flag" fullscreen>
    <v-container fluid fill-height class="loading_bg">
      <v-layout justify-center align-center>
        <v-progress-circular :indeterminate="true" color="accent" />
      </v-layout>
    </v-container>
  </v-dialog>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    nowLoading: {
      type: Boolean,
      default: () => {
        return false
      },
    },
  },
  data() {
    return {
      flag: false,
    }
  },
  watch: {
    nowLoading(val) {
      this.flag = val
    },
  },
})
</script>
""",
                                  name="test", document="test")
        new_repo.add(component=new_component)
        component = new_repo.get(component_id=0)
        assert component
