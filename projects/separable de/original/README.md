# The Original Project
I originally planned the project to have just one example showing the full steps from separation, integration, and simplification. I later decided to show two examples, but ditch the integration process altogether because: (1) this project is not really about integration, and I assume that my viewers already know basic integration, and (2) animating the entire integration process was time-consuming and took more of the video than the actual separation of variables.

# The Files
- `example-separable.py` was the first overall attempt for Example 1 Scene 1. The classes were named `Separable1` all the way up to `Separable9` '(and an extra `Separable12`). The classes had the same animation goal; many classes existed so that each class is a working saved checkpoint, backup, or version. There is no longer anything in this file that was used for the final output.
- `example-separable-reactive.py` was the next attempt for Example 1 Scene 1 which utilized the Reactive Manim extension of ManimCE. Reactive Manim made the transition animations smoother with variable-specific accuracy and targeting. The classes were named `Separable10` to `Separable11` and `Separable13` to `Separable14`. The working version is `Separable13`.
- `parentheses-test (scene2).py` was originally just a file for testing the `Parentheses()` function in Reactive Manim, but later became the file for Scene 2 of Example 1. The classes were named from `Testing` to `Testing4`, which is also the working version.
- `scene3.py` was Scene 3 of Example 1 where the entire integration process should have took place. I made significant progress but had to abandon the idea along the way (as explained earlier).
- `e2-s1.py` and `e2-s2.py` were Scenes 1 and 2 of Example 2 and is now the standard naming convention for `.py` files in the project. Classes in these files are more explicitly defined as attempts. The working versions for these files are `Scene1Attempt2` and `Scene2Attempt4` respectively.

# The Workflow
- Every new unique project must have a named folder in the `projects` folder.
- Files in each project that illustrate examples for the topic must be separated by examples and scenes. 
	- For example, different scenes for Example 1 must have their own dedicated files: `e1-s1.py` (Example 1, Scene 1), `e1-s2.py` (Example 1, Scene 2), etc. This applies to all applicable examples.
- Classes in each file must be separated by attempts. 
	- For example, different attempts for Example 1 Scene 1 should have their classes named `Scene1Attempt1`, `Scene1Attempt2`, etc.
- Animations in each class must be divided by animation identifiers: `AnimA`, `AnimB`, `AnimC` etc.; these correspond to where major equations like `a`, `b`, `c`, etc. are stored. Animation identifiers may be subdivided for minor operations: `AnimA1`, `AnimA2`, etc.; major equations may also be subdivided in the same manner: `a1`, `a2`, etc.