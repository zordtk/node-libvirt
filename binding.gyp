{
    "targets": [
        {
            "target_name": "virt",
            "product_prefix": "lib",
            "cflags!": [
                "<!@(pkg-config --cflags libvirt)",
                "-fno-exceptions"
            ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
            "sources": [
                "src/libvirt.cc",
                "src/worker.cc",
                "src/hypervisor.cc",
                "src/hypervisor-connect.cc",
                "src/hypervisor-domain.cc",
                "src/hypervisor-node.cc",
                "src/domain.cc"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                "."
            ],
            "link_settings": {
                "libraries": [
                    "<!@(pkg-config --libs libvirt)"
                ]
            }
        }
    ]
}
