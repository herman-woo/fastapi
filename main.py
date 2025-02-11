from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import create_db_and_tables, SessionDep
from domains.rater import router as rater_router, RaterRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events in a structured way."""
    print("\n\n           🚀 Starting up...\n\n")
    print("- - - - - - - - - - - - - - - - - - - -\n")
    print("           Workstation - Web")
    print("              Rating Engine")
    print("        Steamboat Insurance Agency\n")
    print("- - - - - - - - - - - - - - - - - - - -\n\n\n\n")
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "                                                                                "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "                              :::::::::::::::                                   "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "                       :::::::::         ::::::                                 "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "                   ::::                      :----:                             "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "                :::                        :-:   :=-:                           "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "             :-=:               ::       :::       :--:                         "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "           :-=-:             ::::::-: ::::-  :        :=-"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "         :==:            :::--      ::  ::  :-         :=-"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "        :=-       :::::--- :+--:    ::        :-        --"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "       :=:       :-   -:=: :-:::::::::         :-:       --"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "       -=        :-   ::--::                     :-       -:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "       =-        --  :::                 ::::     --      :-"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "       -         -=:::    :::::       :---:--:::   -:      :-"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "      ::        -=:   :::--::::::    ----=:  :  :: -+:      -:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "      -        :=   -:-=++-  :: :::-=--=++:  --  :-==:      :-:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     :-        +=::- -=-=++==+- -: :=-= :++==+=  :: ::       -: -:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     --       --:-=: =   ++++= ::  :=:--++-:-- ::   ::       ::-:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     =:       -   -- :-:=*=:- ::    -::---:::       ::       ::  -:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "    :=        =: ::--::::::::::      ::      :::::: ::       :: :-"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "    :=        =-::::::::::                    ::::  ::        : =-:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     =        -=   :         ::    :::           :  --: ::   :--:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     -:       :=:::          :=-::::         :::   ::- :==-:---       ::::::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     :-       -:  :-::         ::              :::: -- -=-=: ::::::::::::::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     :-       -::---:::::::                 :::     =--+--:    -+-:::::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "      -: :   :---:        :::::::::::::::=-         =+==-:    :+*=:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "::    :::=:::--                        ::=- :::-  :-++--:    :+*=:::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "::--: : :-:--:                      :::  :=-:  : :=+=-::   -++*=: ::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "   :--  ::                     *+---**=   =+-  :-==-:    -=***=:  ::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "     :=                     ::-*=::-+=:   ::-----=:   :=+**+=:  :::"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "      --          ::--::   :==-  :::          :--:::-++**+-::::--:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "=---  --      :--==:: =-  =+                     ::-++==-::::::---:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in ": =*--=:      -=*+:   := :+=                                    :-=:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in " :=: :=  ::     =*:    ==-=:                                     :-=:"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in "::  :-: :=:--    :::::::=-:                                        :"]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in " ::--:  := =-                                                     "]))
    print("".join(["\033[31m" + ch + "\033[0m" if ch != " " else " " for ch in ""]))  
    # Initialize DB tables
    create_db_and_tables()
    
    # Ensure tables exists
    with SessionDep() as session:
        RaterRepository(session).create_table()

    yield  # Everything before `yield` runs on startup, everything after runs on shutdown

    print("🛑 Shutting down...")

app = FastAPI(lifespan=lifespan)

# Basic root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"} 

# Register API routes
app.include_router(rater_router, prefix="/rater")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8180)