# AUTO GENERATED FILE - DO NOT EDIT

''NumDisplay <- function(number=NULL, id=NULL) {
    
    props <- list(number=number, id=id)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'NumDisplay',
        namespace = 'bindingtests',
        propNames = c('number', 'id'),
        package = 'bindingtests'
        )

    structure(component, class = c('dash_component', 'list'))
}
