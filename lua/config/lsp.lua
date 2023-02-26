require("mason").setup()
require("mason-lspconfig").setup({
    ensure_installed = {
        "jsonls",
        "lua_ls",
        "pyright",
        "cssls",
        "intelephense",
        "jdtls",
        "omnisharp",
        "rust_analyzer",
        "tsserver",
        "vuels",
        "yamlls",
        "gopls",
    }
})

require("lspconfig").setup({})
