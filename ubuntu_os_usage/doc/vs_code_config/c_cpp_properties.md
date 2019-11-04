# VS Code 设置 c_cpp_properties

## 1. CPP 代码补全.  

安装 "C/C++" 插件.  

Ctrl + Shift + P  => 配置 cpp configuration.

将需要补全的系统头文件路径添加到 "browse" 和 "includePath" 配置项中.  

```json
{
    "configurations": [
        {
            "name": "Linux",
            "browse": {
                "path": [
                    "${workspaceFolder}",
                    "/usr/include",
                    "/usr/local/include",
                    "/usr/include/c++/*",
                    "/usr/include/c++/4.8",
                    "/usr/include/c++/4.8/*",
                    "/usr/include/boost",
                    "/usr/include/boost/**",
                    "/usr/lib/gcc/x86_64-linux-gnu/4.8/include",
                    "/usr/lib/gcc/x86_64-linux-gnu/4.8/include/*",
                    "/usr/include/opencv",
                    "/usr/include/opencv2",
                    "/usr/include/gflags", 
                    "/home/klm/opt/Qt5.10.0/5.10.0/gcc_64/include" 
                ],
                "limitSymbolsToIncludedHeaders": true
            },
            "includePath": [
                "${workspaceFolder}/**",
                "/usr/include",
                "/usr/local/include",
                "/usr/include/c++/*",
                "/usr/include/c++/4.8",
                "/usr/include/c++/4.8/*",
                "/usr/include/boost",
                "/usr/include/boost/**",
                "/usr/lib/gcc/x86_64-linux-gnu/4.8/include",
                "/usr/lib/gcc/x86_64-linux-gnu/4.8/include/*",
                "/usr/include/opencv",
                "/usr/include/opencv2",
                "/usr/include/gflags", 
                "/home/klm/opt/Qt5.10.0/5.10.0/gcc_64/include" 
            ],
            "defines": [],
            "compilerPath": "/usr/bin/clang",
            "cStandard": "c11",
            "cppStandard": "c++14",
            "intelliSenseMode": "clang-x64"
        }
    ],
    "version": 4
}
```