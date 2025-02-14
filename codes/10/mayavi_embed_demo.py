# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Button, Instance
from enthought.traits.ui.api import View, Item, VGroup
from enthought.tvtk.pyface.scene_editor import SceneEditor 
from enthought.mayavi.tools.mlab_scene_model import MlabSceneModel
from enthought.mayavi.core.ui.mayavi_scene import MayaviScene
from enthought.mayavi import mlab

class DemoApp(HasTraits):
    plotbutton = Button("绘图")
    # mayavi场景
    scene = Instance(MlabSceneModel, ()) 
    
    view = View(
        VGroup(
            # 设置mayavi的编辑器
            Item(name='scene',  
                editor=SceneEditor(scene_class=MayaviScene), 
                resizable=True,
                height=250,
                width=400
            ),
            'plotbutton',
            show_labels=False
        ),
        title="在TraitsUI中嵌入Mayavi"
    )
      
    def _plotbutton_fired(self):
        self.plot()
     
    def plot(self):
        mlab.test_mesh() 
    
app = DemoApp()
app.configure_traits()   