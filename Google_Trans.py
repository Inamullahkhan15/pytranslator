# copied and simplified from https://pypi.org/project/googletrans/
import asyncio  # built-in module for asynchronous programming where we can run multiple tasks at the tasks at the same time

from googletrans import Translator


# Using asyncio we can run tasks asynchronously, meaning: the program will do something else while waiting (e.g., for a network request).
# Very useful in web apps, I/O, or real-time systems.
# Without asyncio, the program might "freeze" waiting for slow operations like downloading or translating.
async def translate_text():  # asynchronous function means it can run in the background
    # async tells Python "This function is a coroutine or an asynchronous funcition
    # and it will be doing things that don’t need to block/freeze the program. So, be careful"
    async with (
        Translator() as translator
    ):  # with means it will automatically close the translator when done
        # 'sync' here means it will run synchronously, meaning it will wait for the result before moving on
        # this is needed Translator() may take time to initialize and connect to the Google Translate API
        # and we don't want to block the program while waiting for it.
        # It is just like saying: "Ruko Zara, Sabar Karo !"

        # with - a context manager it ensures that the resources are properly managed.
        # it automatically opens and closes resources (database connections, files, I/O Operations, Network requests, etc.)
        # It is like a "try-finally" block, but cleaner and more readable.
        # Here 'with' is used to create a Translator object that will be automatically closed after use.

        # as : assigns the result to the variable translator
        # just like translator = Translator() but it will automatically close the translator when done

        result = await translator.translate(
            "Man gets what he strives for!", dest="FR"
        )  # await means it will wait for the result
        # translate() method is used to translate the text
        # dest='FR' means we want to translate to French
        # If we don't specify dest, it will detect the language automatically.

        # 'wait' means “Wait here until this task is done, but don’t block the rest of the system.”
        # it pauses the function temporarily and resumes when the task completes (e.g., network call).
        # Without 'await', we get a coroutine object instead of the real result.

        print(result)
        print(f"Original: {result.origin}")
        print(f"Translated: {result.text}")
        print(f"Detected Language: {result.src}")


asyncio.run(translate_text())  # asyncio.run() is used to run the asynchronous function
# 'asyncio.run() means to say, “Hello asyncio, please start and manage this async process for me.”
# 'run()' starts, runs and closes the async function (aka coroutine) and returns the result.
