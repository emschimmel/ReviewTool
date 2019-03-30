
class Config():
    git_base_branch = "master"
    gitpath = "gitdump/branches"
    gitpath_with_master = gitpath+"/"+git_base_branch
    git_url = "https://github.com/emschimmel/kweb"
    bad_words = ["var ", "mutable", "throw", "constructor", "new", "if", "= null", "=null", ".*", "= Arraylist", "System.out.println"]
    warning_words = [".forEach", ".add", ".put", "print", "println"]
    compliment_words = [".map", "data class", "enum class", "companion object", "when(", "when (", "?:", "listof", "setof", "mapof", ".let", "private val"]
    allowed_file_extentions = ["kt", "txt", "yml", "md", "pom", "xml", "json", "gradle", "bat", "gitignore", "LICENSE", "gradlew"]
    directories_to_ignore = [".git", ".idea"]