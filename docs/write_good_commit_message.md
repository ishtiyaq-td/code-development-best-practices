# Write Good Commit Message

1. Commit message must have a **Subject** and a **Body**
2. Separate subject from the body with a blank line
3. Limit the subject line to 50 characters
4. Do not end the subject line with a period
5. Use the steps mentioned in the Writing subject line section.
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

## Writing subject line

This a syntax of commit subject:

`COMMIT_TYPE: IMPERATIVE MESSAGE`

**Commit Types are:**

1. NEW

2. IMPROVE

3. FIX

4. DOC

5. RELEASE

6. TEST

**Imperative message should start with following words with Capitalization as given:**

1. Add

2. Update

3. Delete

4. Fix

5. Rename

6. Style

7. Test

**A properly formed Git commit imperative message should always be able to complete the following sentence:**

If applied, this imperative message will `<your imperative message here>`

## Add emojis to your messages

Edit your `.gitconfig` file located in your home directory.

```bash
vi ~/.gitconfig
```

Paste the following lines and save:

```bash
[alias]
    logg = log --oneline --graph --decorate

# git commit, add all and push — in one step.
cap = "!f() { git commit -e -m \"$@\"; }; f"

# initial commit
int = "!f() { git cap \"🎉 INITIAL: $@\"; }; f"
# new file
new = "!f() { git cap \"📦 NEW: $@\"; }; f"
# improved code
imp = "!f() { git cap \"👌 IMPROVE: $@\"; }; f"
# bug fixes
fix = "!f() { git cap \"🐛 FIX: $@\"; }; f"
# code release
rlz = "!f() { git cap \"🚀 RELEASE: $@\"; }; f"
# document created
doc = "!f() { git cap \"📖 DOC: $@\"; }; f"
# test cases written
tst = "!f() { git cap \"✅ TEST: $@\"; }; f"
# created new tag
tagg = "!f() { git cap \"🔖 TAG: $@\"; }; f"
```

### Use following commands to commit

If you wish to commit new changes, use the following command


```bash
git int "Imperative message"
```

```bash
git new "Imperative message"
```

If you wish to commit improved code changes, use the following command

```bash
git imp "Imperative message"
```

If you wish to commit any bug fixes, use the following command

```bash
git fix "Imperative message"
```

If you wish to commit a relese, use the following command

```bash
git rlz "Imperative message"
```

If you wish to commit a doc related changes, use the following command

```bash
git doc "Imperative message"
```

If you wish to commit test code related changes, use the following command

```bash
git tst "Imperative message"
```

If you want to see the list of subjects from commits, use the following command

```bash
git logg
```

#### Include commit references and issues in git messages

```bash
To refer a commit in git message, copy hexsha(copy 7 or more than 7 characters) of a commit message, and add to the commit message.(eg. 321db27)
```

```bash
To refer an issue on gitlab in git message, copy id of the issue.(eg. #1)
```

#### Example of a good commit

This is how you should write a good commit message.

```bash
git imp "Update assignment's hide unhide code"
```

and press enter, It will open a text editor. Here you can write your full commit message as per example shown below.

```bash
👌 IMPROVE: Update assignment's hide unhide code

This commit fix issue #1 the performance problem of hiding and unhiding assignment related to commit 321db27.
The page doesn't refresh after clicking the hide/unhide button.

Following things are done:
 - Add asynchronous script to button UI
 - Change the text status on the button
```
