#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
import linecache

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


if __name__ == "__main__":
    filename = "account.txt"

    username = linecache.getline(filename, 1)
    password = linecache.getline(filename, 2)
    api = InstagramAPI(username, password)
    api.login()

    user_id = api.username_id

    # List of all followers

    followers = getTotalFollowers(api, user_id)
    print('Follower info:',(followers))


   # optionally getting the follower amount
    followers = api.getTotalFollowers(user_id)
    print('Number of followers:', len(followers))

    with open('followers.txt', 'w') as f:
        for item in followers:
            f.write("%s\n\n" % item)
