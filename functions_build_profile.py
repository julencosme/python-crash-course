def build_profile(first, last, **user_info):
    """Build a profile dictionary containing user information."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'Johnny', 'Witherspoon', location='MIT', field='computational sciences')
print(user_profile)
