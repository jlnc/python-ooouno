# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt.tree
from __future__ import annotations
from .x_tree_control import XTreeControl as XTreeControl_e0500cfb

class TreeControl(XTreeControl_e0500cfb):
    """
    Service Class

    A control that displays a set of hierarchical data as an outline.
    
    A specific node in a tree is identified by a XTreeNode. A leaf node is a node without any children and that returns FALSE when calling XTreeNode.hasChildrenOnDemand(). An expanded node is a non-leaf node that will displays its children when all its ancestors are expanded. A collapsed node is one which hides them. A node is visible when all parent nodes are expanded and the node itself is in the display area.
    
    The nodes are retrieved from a XTreeDataModel. You can implement it yourself or use the MutableTreeDataModel which uses XMutableTreeNode and XMutableTreeDataModel for a simple and mutable data model.
    
    The data model must be set at the TreeControlModel.TreeDataModel property.
    
    If you are interested in knowing when the selection changes implement a com.sun.star.view.XSelectionChangeListener and add the instance with the method com.sun.star.view.XSelectionSupplier.addSelectionChangeListener(). You than will be notified for any selection change.
    
    If you are interested in detecting either double-click events or when a user clicks on a node, regardless of whether or not it was selected, you can get the com.sun.star.awt.XWindow and add yourself as a com.sun.star.awt.XMouseClickHandler. You can use the method XTreeControl.getNodeForLocation() to retrieve the node that was under the mouse at the time the event was fired.
    
    If you want to add child nodes to your tree on demand you can do the following.
    
    Now you get called when the node will become expanded or collapsed. So on XTreeExpansionListener.treeExpanding() you can check the TreeExpansionEvent if the parent node with children on demand is going to be expanded and in that case add the missing child nodes. You can also veto the expansion or collapsing of a parent node by using the ExpandVetoException.

    See Also:
        `API TreeControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1tree_1_1TreeControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.TreeControl'
    __ooo_type_name__: str = 'service'


__all__ = ['TreeControl']

