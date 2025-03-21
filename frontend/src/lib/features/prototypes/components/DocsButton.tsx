import { Modal, ModalDialog } from '@mui/joy';
import { BookText, Check, Copy, Loader2, Pencil, Save, X } from "lucide-react";
import { useState } from "react";

export function DocsButton() {
    const [showDocsModal, setShowDocsModal] = useState(false);
    const [docs, setDocs] = useState("");
    const [docsLoading, setDocsLoading] = useState(false);
    const [copied, setCopied] = useState(false);
    const [editing, setEditing] = useState(false);

    const showDocs = async () => {

        if (docs.length > 0) {
            setShowDocsModal(true);
            return;
        }

        setDocsLoading(true);
        await new Promise((resolve) => setTimeout(resolve, 2000));
        setDocs(`
# UML Prototype Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Design Goals](#design-goals)
4. [UML Diagrams](#uml-diagrams)
   - [Class Diagram](#class-diagram)
   - [Sequence Diagram](#sequence-diagram)
   - [Use Case Diagram](#use-case-diagram)
   - [Activity Diagram](#activity-diagram)
5. [Component Descriptions](#component-descriptions)
6. [Assumptions and Constraints](#assumptions-and-constraints)
7. [Future Enhancements](#future-enhancements)
8. [References](#references)

---

## Introduction

This document provides an overview and detailed description of the UML prototype. It is intended to help developers, designers, and stakeholders understand the system architecture, relationships, and interactions.

    `);
        setShowDocsModal(true);
        setDocsLoading(false);
    };

    const closeDocs = () => {
        setShowDocsModal(false);
    };

    const copyDocs = () => {
        navigator.clipboard.writeText(docs);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <>
            <button
                onClick={showDocs}
                className="w-[80px] h-[40px] bg-stone-200 rounded-md hover:bg-stone-300 flex items-center justify-center shrink-0"
            >
                {docsLoading ? <Loader2 className="animate-spin size-4 mr-2 shrink-0" /> : <BookText className="size-4 mr-2 shrink-0" />}
                Docs
            </button>

            <Modal open={showDocsModal} onClose={closeDocs}>
                <ModalDialog className="max-h-screen overflow-y-auto">
                    <div className="flex gap-2 items-center justify-between">
                        <button
                            onClick={closeDocs}
                            className="w-[40px] h-[40px] bg-gray-500 text-white rounded-md hover:bg-gray-600 flex items-center justify-center shrink-0"
                        >
                            <X className="size-5" />
                        </button>

                        <div className="flex gap-2">


                        <button
                                onClick={() => {
                                    setEditing(!editing);
                                    console.log("Editing: ", editing);

                                }}
                            className="w-[40px] h-[40px] bg-gray-500 text-white rounded-md hover:bg-gray-600 flex items-center justify-center shrink-0"
                        >
                                {!editing ? (<Pencil className="size-5" />) : (

<svg xmlns="http://www.w3.org/2000/svg" className="size-5" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pencil-off"><path d="m10 10-6.157 6.162a2 2 0 0 0-.5.833l-1.322 4.36a.5.5 0 0 0 .622.624l4.358-1.323a2 2 0 0 0 .83-.5L14 13.982"/><path d="m12.829 7.172 4.359-4.346a1 1 0 1 1 3.986 3.986l-4.353 4.353"/><path d="m15 5 4 4"/><path d="m2 2 20 20"/></svg>

                            )}
                            </button>


                            <button
                                onClick={() => { }}
                            className="w-[40px] h-[40px] bg-gray-500 text-white rounded-md hover:bg-gray-600 flex items-center justify-center shrink-0"
                        >
                            <Save className="size-5" />
                            </button>

                            <button
                            onClick={copyDocs}
                            className="w-[40px] h-[40px] bg-gray-500 text-white rounded-md hover:bg-gray-600 flex items-center justify-center shrink-0"
                            >
                            {copied ? <Check className="size-5" /> : <Copy className="size-5" />}
                            </button>

                            </div>
                    </div>

                    <div className="flex h-full w-full flex-col gap-1 p-3">
                        <pre contentEditable={editing}>{docs}</pre>
                    </div>
                </ModalDialog>
            </Modal>
        </>
    );
}
