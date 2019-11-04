# VS Code 用户偏好设置

## (1) 需要提前安装的插件 

- C/C++   
- Markdown Preview Enhanced   
- python   
- C/C++ Clang Command Adapter   
- jupyter   
- vscode-icons  

## (2) 配置 settings.json 文件  

将以下内容添加到 settings.json 文件中.  

```json
{
    "workbench.colorTheme": "Monokai",
    "editor.minimap.enabled": false,
    "editor.renderWhitespace": "all",

    "workbench.sideBar.location": "left",
    "editor.rulers": [79],
    "files.autoSave": "onFocusChange",
    "editor.wordWrap": "on",
    "extensions.ignoreRecommendations": true,

    // 打字很卡
    "search.followSymlinks": false,
    
    // cpp configurations
    // 不显示错误信息  
    "C_Cpp.errorSquiggles": "Disabled",
    // Controls whether the IntelliSense engine will automatically switch to the Tag Parser for translation units containing #include errors.
    "C_Cpp.intelliSenseEngineFallback": "Enabled",
    "C_Cpp.dimInactiveRegions": false,

    // Clang command or the path to the Clang executable
    "clang.executable": "/usr/bin/clang-6.0",
    "clang.completion.enable": true,
    "clang.cxxflags": [
        "-std=c++11",
        "-I/usr/include/",
        "-I/usr/include/c++/4.8/",
        "-I/usr/include/boost/"
    ],
    "clang.cflags": [
        "-std=c99",
        "-Ic:/usr/include",
    ],

    // When enabled, Emmet abbreviations are expanded when pressing TAB.
    "emmet.triggerExpansionOnTab": true,
    "workbench.statusBar.feedback.visible": false,

    "[cpp]": {
      "editor.quickSuggestions": true
    },
    "[c]": {
        "editor.quickSuggestions": true
    },
    "window.zoomLevel": 0,

    // Choose the Math expression rendering method here. You can also disable math rendering if you want by choosing 'None'.
    "markdown-preview-enhanced.mathRenderingOption": "MathJax",
    "editor.largeFileOptimizations": false,

    // python
    "python.pythonPath": "/usr/bin/python3",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pep8Enabled": false,
    "python.jediEnabled": false,

    // python auto complete
    "python.autoComplete.extraPaths": [
        "/usr/local/lib/python3.5/dist-packages/",
        "/home/magic/work/pyenv/dl/lib/python3.5/site-packages/"
    ],
    // Automatically add brackets for functions.
    "python.autoComplete.addBrackets": true,
    // Insert snippets when their prefix matches. Works best when 'quickSuggestions' diabled.
    "editor.tabCompletion": true,

    "explorer.confirmDelete": false,
    "workbench.iconTheme": "vscode-icons",
    "markdown-preview-enhanced.mermaidTheme": "dark",
    "markdown-preview-enhanced.previewTheme": "github-dark.css",
    "markdown-preview-enhanced.revealjsTheme": "night.css"
}
```


## 3. markdown style 设置  

```json
/* Please visit the URL below for more information: */
/*   https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css */ 

.markdown-preview.markdown-preview {
  // modify your style here
  // eg: background-color: blue;  
  background-color: rgba(8, 170, 148, 0.932);  
}
```