# Topic map

Which videos feed which doc. P1 = "Tosca Tutorial from Scratch" (LambdaGeeks, Part N).
P2 = QASCRIPT "Tosca Tutorial" (Lesson N; "v2" = the Tosca 16 features video, "live" = live sessions).
Ids are in `raw/manifest.json`. Update this file when docs are added or merged.

## getting-started (level 1)
| doc | sources |
|---|---|
| what-is-tosca | P1-1, P2-L1 |
| architecture | P1-1 |
| licensing | P1-2, P2-L2, P2 "Setup with trial cloud license" |
| installation | P1-2, P2-L3 (AWS EC2 / Windows Server) |
| workspace-and-project-setup | P1-3, P2-L5 |
| commander-overview | P1-3, P2-L4 |
| first-test-case | P2-L4, P2-L5 |
| whats-new-in-tosca-16 | P2 v2 |

## modules (level 1)
| doc | sources |
|---|---|
| modules-overview | P1-4 |
| xscan | P1-4, P2-L6 |
| control-identification | P2-L6 (anchor), L7 (image), L8 (index), L43 (explicit name) |
| rescan-modules | P2-L9 |
| duplicate-and-merge-modules | P2-L10, L104 |
| module-properties-and-parameters | P2-L157 (configuration / identification / steering params) |
| table-controls | P2-L155, L45 (embedded), L46 (row/column count) |
| table-baseline-comparison | P2-L47 |

## test-cases (level 1)
| doc | sources |
|---|---|
| test-case-basics | P1-5 |
| action-modes | P1-11, P2-L29 (Buffer), L30 (WaitOn), L31 (Select/Constraint/Verify) |
| control-flow | P2-L32 (If), L33 (Do/While) |
| repetitions | P2-L48 |
| recovery-and-cleanup-scenarios | P2-L49, L50 |
| recorder | P2-L75 |
| exploratory-testing | P2-L76 |

## test-case-design (level 2)
| doc | sources |
|---|---|
| test-case-design-overview | P1-10 |
| test-sheets-and-attributes | P2-L52 |
| instances-and-combinatorics | P2-L53, L54 |
| templates-and-instantiation | P2-L55, L56, L57 |
| design-classes | P1-10, P2-L58 |
| worked-example-end-to-end | P2 live "Test Case Designing" |

## standard-modules (level 2)
| doc | sources |
|---|---|
| file-and-folder-operations | P2-L11, L12 |
| buffer-operations | P2-L13 |
| start-and-close-programs | P2-L14, L15, L27 (clear Chrome cache) |
| evaluation-tool | P2-L16, L126 |
| screenshots-on-failure | P2-L17 |
| window-operations | P2-L18, L25 (scroll), L122 (close popup) |
| desktop-dialogs | P2-L24 |
| execute-javascript | P2-L26 |

## engines (level 3)
| doc | sources |
|---|---|
| excel-engine | P2-L19, L20, L21 |
| pdf-engine | P2-L22, L23, L146 |
| xml-engine | P2-L28, L118, L134 |
| uia-engine-and-desktop | P2-L142, L143 (JS alert) |

## expressions (level 2)
| doc | sources |
|---|---|
| random-values | P2-L34, L117, L119, L137 |
| date-expressions | P2-L36, L38, L120, L123, L135, L139 |
| string-operations | P2-L39, L40, L41, L148 |
| intervals-and-verification-expressions | P2-L37, L35 (multilingual, regex), L140 (regex) |

## execution (level 2)
| doc | sources |
|---|---|
| execution-lists | P1-6, P2-L59, L61 |
| execution-results-and-logs | P2-L60, L62, L63, L64, L69 |
| manual-execution | P2-L65, L66 |
| execution-repetitions-and-business-test-cases | P2-L67, L68 |
| recording-executions | P2-L70 |
| scheduling-executions | P2-L141 |
| cross-browser-execution | P2-L144, L143b (no feasible executor) |
| dokusnapper | P1-6 |
| ci-integration-jenkins | P2-L89 |
| distributed-execution-dex | P2-L152 |
| tosca-execution-client | P2-L153 |

## data-and-parameters (level 2)
| doc | sources |
|---|---|
| buffers | P1-9, P2-L77 (Buffer Viewer), L116 (XBuffer) |
| test-configuration-parameters | P1-7, P2-L156, L106 (multiple tabs, ConstraintIndex section) |
| business-parameters-and-libraries | P1-8, P2-L51 |
| test-data-services | P2-L154 (concept, web UI, {TDS[]} syntax) |
| test-data-service-modules | P2-L154 from 22:27 (Modules, CRUD flow, Expert Module) |

## api-testing (level 3)
| doc | sources |
|---|---|
| api-scan-basics | P1-12, P2-L79, L80 |
| api-test-cases | P1-13, P2-L81, L82 |
| api-authentication | P2-L83, L84 |
| api-message-structure-and-soap | P2-L85, L86, L87 |
| api-message-recorder | P2-L88 |

## requirements-and-reporting (level 3)
| doc | sources |
|---|---|
| requirements-and-risk | P2-L71, P2 live "Requirements Management" |
| reports | P2-L72 |
| tql-and-virtual-folders | P2-L73 |
| import-from-excel | P2-L74 |

## administration (level 4)
| doc | sources |
|---|---|
| users-and-groups | P1-14, P2-L91 |
| multi-user-workspaces | P2-L90, L95 (checkout details), L138 (synchronization policy, currently in best-practices/synchronisation-not-waits) |
| branches | P2-L92 |
| backup-and-restore | P2-L93 |
| command-line-tools | P2-L78 (TCShell), L94 (TCWorkspaceUtil) |
| test-mandates | P2-L96 |
| versioning-and-recovery | P2-L145 |
| tosca-server | P2-L151 |

## best-practices (level 3)
| doc | sources |
|---|---|
| naming-conventions | P2-L97 |
| test-case-structure | P2-L98 (verification points), L103 (folders), L102 (loops), L105 (workstates) |
| module-hygiene | P2-L99 (limited attributes), L104 (merge duplicates) |
| synchronisation-not-waits | P2-L100, L101 (L138 synchronization policy is covered there for now; it belongs to multi-user workspaces) |
| review-process | P2-L106b |

## troubleshooting (level 3)
| doc | sources |
|---|---|
| obstacles-identification | P2-L107, L108, L110, L112, L113, L130, L131 |
| obstacles-tables | P2-L109, L111, L115, L124, L125, L127, L128, L129 |
| obstacles-input-and-clicks | P2-L114, L121, L132, L133, L136 |
| common-problems-and-fixes | P2-L147, L149, L150 |
| worked-example-live-project | P2 live "Automate End-to-End Scenarios" |

## reference
glossary, learning-path, action-modes cheat sheet, expressions cheat sheet.

---

# Playlist 3: "TRICENTIS Tosca Automation Tutorial" (FicusRoot, Tosca 16) — P3-L<N>

Ingested 2026-09-04 as subtitle transcripts. Two compilation videos (QDV_Tl0_JyU "Beginners Full Course",
SeRVcyMWhkQ "Advanced Full Course") are excluded: they repeat the lessons. Most lessons overlap P1/P2;
they were merged into the existing docs below (Tosca 16 UI differences, extra examples). New docs are marked NEW.

| target doc | P3 lessons |
|---|---|
| getting-started/installation, licensing | L1 |
| getting-started/commander-overview | L2 |
| getting-started/workspace-and-project-setup | L3 (workspace, subset .tsu import) |
| getting-started/tosca-automation-extension (NEW) | L4 (browser extension, SUT intro) |
| getting-started/what-is-tosca, standard-modules/index | L5 (model-based, standard modules) |
| getting-started/agentic-test-automation (NEW) | "Tosca Agentic Test Automation Explained" (RH2F4nkOj64) |
| modules/xscan | L6 |
| modules/control-identification | L7 (properties, anchor), L23 (dynamic ID, explicit name), L24 (explicit name, ResultCount) |
| modules/control-groups (NEW) | L7 (control groups part) |
| modules/rescan-modules, duplicate-and-merge-modules | L15 (rescan, merge) |
| modules/module-properties-and-parameters | L15 (value range) |
| modules/table-controls | L30 |
| modules/table-baseline-comparison | L76 (obstacle 34) |
| test-cases/test-case-basics, getting-started/first-test-case | L8, L9, L10, L11 |
| test-cases/action-modes | L12 (WaitOn, Verify, Select), L25 (Constraint), L13/L13-updated (Buffer) |
| test-cases/control-flow | L19, L27, L28, L29 |
| test-cases/repetitions | L24 (folder repetition) |
| test-cases/recovery-and-cleanup-scenarios | L20, L21 |
| execution/self-healing (NEW) | L26 (self-healing mode) |
| data-and-parameters/buffers | L13/L13-updated (Buffer ActionMode), L22 (XBuffer) |
| data-and-parameters/test-configuration-parameters | L11 (TCP) |
| data-and-parameters/business-parameters-and-libraries | L14 (TestStepLibrary), L16 (business parameters) |
| expressions/random-values, string-operations, date-expressions, intervals-and-verification-expressions | L13 (math), L33 (multilingual regex), L34 (intervals), L38, L39 (strings), L53, L55, L56, L59, L62, L71 (obstacle expressions) |
| execution/execution-lists | L17 |
| requirements-and-reporting/requirements-and-risk | L18 (link TestCases / ExecutionLists to requirements) |
| standard-modules/screenshots-on-failure, start-and-close-programs, window-operations | L31, L32, L58 |
| engines/excel-engine | L35, L36 |
| engines/xml-engine | L54, L70 |
| engines/mobile-testing-and-device-cloud (NEW) | Device Cloud (hGO8dCyu0sY, a6byhLYJuJU), Mobile L5 (wpkwzSAGpgs), Mobile L6 (ohfGxtWWRno) |
| administration/multi-user-workspaces, users-and-groups, branches | L40, L41, L42 |
| troubleshooting/obstacles-* , common-problems-and-fixes | L37, L43–L75 (obstacles 1–33; 32 "sort numbers" and 33 "play game" are new) |
